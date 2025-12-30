from main import app
from database import db
from sqlalchemy import inspect, text

def check_tables():
    with app.app_context():
        print("Checking database for tables...")
        try:
            # Use SQLAlchemy inspector to get table names
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            print(f"Found {len(tables)} tables:")
            for table in tables:
                print(f" - {table}")
            
            if 'destination' in tables or 'DESTINATION' in tables:
                print("\n[CONFIRMED] 'destination' table exists.")
                
                # Optional: Check row count
                with db.engine.connect() as conn:
                    result = conn.execute(text("SELECT COUNT(*) FROM destination"))
                    count = result.scalar()
                    print(f"Table 'destination' has {count} rows.")
            else:
                print("\n[WARNING] 'destination' table was NOT found.")
                
        except Exception as e:
            print(f"Error checking tables: {e}")

if __name__ == "__main__":
    check_tables()
