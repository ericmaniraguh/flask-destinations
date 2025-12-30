from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, inspect

db = SQLAlchemy()

def init_db(app):
    # Configure Database
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        "oracle+oracledb://auca_admin:admin@localhost:1521/?service_name=class_2025_pdb"
    )
    
    db.init_app(app)
    
    with app.app_context():
        try:
            # Check connection
            db.session.execute(text('SELECT 1 FROM DUAL'))
            print("\n-----------------------------------------------------------")
            print(" [SUCCESS]: Connected to Oracle Database!")
            
            # Check availability of tables
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f" [INFO]: Available tables: {tables}")

            print("-----------------------------------------------------------\n")
            db.create_all()
        except Exception as e:
            print("\n-----------------------------------------------------------")
            print(" [FAILED]: Could not connect to Oracle Database.")
            print(f"Error: {e}")
            print("-----------------------------------------------------------\n")
