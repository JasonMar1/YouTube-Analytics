from app.routes import app
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 for local dev
    app.run(host='0.0.0.0', port=port)
    app.run(debug=False)
