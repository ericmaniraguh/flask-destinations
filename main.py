from flask import Flask
from flask_cors import CORS
from database import init_db
from routes import main_bp

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Initialize Database
init_db(app)

# Register Blueprint
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode - everytime i change code
