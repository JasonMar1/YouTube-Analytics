# data_processor.py
from app import db
from app.models import DeviceType, Day, Gender, Month, SharingService, UploaderType, Video
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime


def save_to_db(data, db, table_name, user_id):
    # Mapping table names to models
    table_model_map = {
        'deviceType': DeviceType,
        'day': Day,
        'gender': Gender,
        'month': Month,
        'sharingService': SharingService,
        'uploaderType': UploaderType,
        'video': Video
    }

    # Get the model class based on the table name
    model_class = table_model_map.get(table_name)
    if model_class is None:
        raise ValueError(f"No model found for table: {table_name}")

    # Create a list of columns in the table
    column_headers = [header['name'] for header in data['columnHeaders']]

    # Use the first column as the criteria for checking uniqueness
    first_column = column_headers[0]

    # Extract rows from data
    rows = data['rows']

    # Iterate over rows and create instances of the model
    for row in rows:
        try:
            # Prepare the criteria for checking if a record exists
            criteria = {first_column: row[0]}  # Only include the first column value in criteria

            # Remove empty string and 'null' from criteria
            if isinstance(criteria[first_column], str) and criteria[first_column].lower() in {'null', ''}:
                criteria[first_column] = None

            # Check if the record already exists
            existing_record = db.session.query(model_class).filter_by(user_id=user_id, **criteria).first()

            if existing_record is None:
                # Create an instance of the model class with the appropriate fields
                entry = model_class(user_id=user_id)
                for header, value in zip(column_headers, row):
                    if isinstance(value, str) and value.lower() in {'null', ''}:
                        value = None
                    if header == 'day':
                        try:
                            value = datetime.strptime(value, '%Y-%m-%d').date()
                        except (ValueError, TypeError):
                            value = None
                    elif header == 'month':
                        try:
                            datetime.strptime(value, '%Y-%m')
                            value = str(value)
                        except (ValueError, TypeError):
                            value = None
                    setattr(entry, header, value)

                # Add the instance to the session
                db.session.add(entry)
            else:
                print(f"Record already exists for {table_name} with criteria: {criteria}")

        except Exception as e:
            print(f"Error processing data for table {table_name}: {str(e)}")
            continue

    # Commit the transaction
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Database commit error: {str(e)}")

    print(f"Data has been saved to the {table_name} table.")
