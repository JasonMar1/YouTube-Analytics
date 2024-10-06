from app.routes import app
import os
import logging

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 for local dev
    app.run(host='0.0.0.0', port=port)

    app.run(debug=True)


    # Configure logging
    logging.basicConfig()
    logger = logging.getLogger('sqlalchemy.engine')
    logger.setLevel(logging.INFO)  # Use DEBUG for more detailed logs

    # Optional: Configure logging format
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

