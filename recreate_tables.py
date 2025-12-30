from main import app
from database import db
from sqlalchemy import text

def recreate_tables():
    with app.app_context():
        print("Recreating tables...")
        try:
            # 1. Drop existing table
            print("Dropping 'destination' table and sequence if they exist...")
            # Note: db.drop_all() might be safer, but let's target what we changed
            db.drop_all() 
            
            # 2. Create tables with new model definition (including Sequence)
            print("Creating tables...")
            db.create_all()
            
            print("[SUCCESS]: Tables recreated with Sequence configuration.")
            
        except Exception as e:
            print(f"[FAILED]: Error recreating tables: {e}")

if __name__ == "__main__":
    recreate_tables()
