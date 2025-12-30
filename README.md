# Python API - Destination Manager

This is a Flask-based REST API designed to manage travel destinations. It allows users to perform CRUD (Create, Read, Update, Delete) operations on destination data, including fields for destination name, country, rating, and image URL. The application uses an Oracle Database for data persistence.

## Technologies Used

- **Python**: Core programming language.
- **Flask**: Micro web framework for building the API.
- **SQLAlchemy / Flask-SQLAlchemy**: ORM for database interaction.
- **Oracle Database**: Backend database (accessed via `oracledb`).
- **Postman/CURL**: Recommended for testing API endpoints.

## Prerequisites

- Python 3.x installed.
- Access to an Oracle Database instance.
- Oracle Instant Client (if required by your environment).

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Create a Virtual Environment** (recommended):

    ```bash
    python -m venv api_env
    # Windows
    api_env\Scripts\activate
    # macOS/Linux
    source api_env/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The database connection is currently configured in `database.py`.

- **Database URI**: The application connects to a local Oracle database.
  ```python
  # database.py
  app.config['SQLALCHEMY_DATABASE_URI'] = (
      "oracle+oracledb://auca_admin:admin@localhost:1521/?service_name=class_2025_pdb"
  )
  ```
  _Note: Ensure your local Oracle database matches these credentials (`auca_admin`/`admin`) or update the `database.py` file with your specific configuration._

## Running the Application

1.  **Start the Flask development server**:
    ```bash
    python main.py
    ```
2.  The API will be accessible at `http://localhost:5000`.

## API Endpoints

### 1. Home

- **URL**: `/`
- **Method**: `GET`
- **Description**: Basic health check, returns "Hello World".

### 2. Get All Destinations

- **URL**: `/destinations`
- **Method**: `GET`
- **Description**: Retrieves a list of all destinations.
- **Response**: JSON array of destination objects.

### 3. Get Single Destination

- **URL**: `/destinations/<id>`
- **Method**: `GET`
- **Description**: Retrieves a specific destination by its ID.

### 4. Create Destination

- **URL**: `/destinations`
- **Method**: `POST`
- **Description**: Creates a new destination.
- **Body** (JSON):
  ```json
  {
    "destination": "Kigali",
    "country": "Rwanda",
    "rating": 4.8,
    "image": "https://example.com/kigali.jpg"
  }
  ```

### 5. Update Destination

- **URL**: `/destinations/<id>`
- **Method**: `PUT`
- **Description**: Updates an existing destination. Fields are optional (partial update).
- **Body** (JSON):
  ```json
  {
    "rating": 4.9
  }
  ```

### 6. Delete Destination

- **URL**: `/destinations/<id>`
- **Method**: `DELETE`
- **Description**: Deletes a destination by its ID.

### 7. Create Multiple Destinations (Batch)

- **URL**: `/destinations/batch`
- **Method**: `POST`
- **Description**: Creates multiple destinations in a single request.
- **Body** (JSON):
  ```json
  [
    {
      "destination": "Paris",
      "country": "France",
      "rating": 4.8,
      "image": "url1"
    },
    {
      "destination": "Tokyo",
      "country": "Japan",
      "rating": 4.9,
      "image": "url2"
    }
  ]
  ```

## Postman Collection

You can test these API endpoints using the provided Postman collection:
[**Run in Postman**](https://www.postman.com/ericpostman-robot-651831/workspace/restapi-flask-destination/collection/16012276-c4602524-f9e4-49aa-b43d-7f16a3b8910f?action=share&creator=16012276)

## Database Helper Scripts

Several scripts are included to help manage the database:

- `recreate_tables.py`: **CAUTION**. Drops the `destination` table and recreates it. Useful for resetting the schema (e.g., adding sequences for Auto-Increment).
- `check_tables.py`: Checks connection and lists available tables in the database.
- `seed_destinations.py`: Adds sample data (8 destinations) to the database for testing.

## Project Structure

- `main.py`: Entry point of the application. Initializes the app and registers blueprints.
- `routes.py`: Defines the API endpoints and logic.
- `models.py`: Defines the database schema (SQLAlchemy models).
- `database.py`: Handles database connection and initialization.
- `requirements.txt`: List of python dependencies.
