from main import app
from database import db
from models import Destination
from sqlalchemy.schema import CreateTable

def create_tables():
    with app.app_context():
        # 1. Generate and print the SQL Statement
        # This shows you the raw SQL that SQLAlchemy will use
        print("--- SQL/DDL Statement ---")
        sql = CreateTable(Destination.__table__).compile(db.engine)
        print(sql)
        print("-------------------------\n")

        # 2. Create the tables in the database
        print("Creating tables in database...")
        try:
            db.create_all()
            print("Successfully created tables (if they didn't exist).")
        except Exception as e:
            print(f"Error creating tables: {e}")

if __name__ == "__main__":
    create_tables()
