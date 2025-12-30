from main import app
from database import db
from models import Destination

def seed_data():
    destinations_data = [
        {
            "destination": "Kigali",
            "country": "Rwanda",
            "rating": 4.5,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Kigali_Convention_Centre_%28KCC%29.jpg/640px-Kigali_Convention_Centre_%28KCC%29.jpg"
        },
        {
            "destination": "Paris",
            "country": "France",
            "rating": 4.8,
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/47/New_york_times_square-terabass.jpg"
        },
        {
            "destination": "Tokyo",
            "country": "Japan",
            "rating": 4.9,
            "image": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Skyscrapers_of_Shinjuku_2009_January.jpg"
        },
        {
            "destination": "New York",
            "country": "USA",
            "rating": 4.7,
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu.jpg/640px-View_of_Empire_State_Building_from_Rockefeller_Center_New_York_City_dllu.jpg"
        }
    ]

    with app.app_context():
        print(f"Adding {len(destinations_data)} new destinations to the database...")
        success_count = 0
        for data in destinations_data:
            try:
                # Check if it already exists to avoid duplicates is skipped for simplicity
                new_dest = Destination(
                    destination=data['destination'],
                    country=data['country'],
                    rating=data['rating'],
                    image=data['image']
                )
                db.session.add(new_dest)
                success_count += 1
            except Exception as e:
                print(f"Error adding {data['destination']}: {e}")
        
        try:
            db.session.commit()
            print(f"[SUCCESS]: Successfully added {success_count} destinations.")
        except Exception as e:
            db.session.rollback()
            print(f"[FAILED]: Error committing to database: {e}")

if __name__ == "__main__":
    seed_data()
