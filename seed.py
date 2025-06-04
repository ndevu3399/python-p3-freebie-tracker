# seed.py

import os
from database import Session, engine, Base
from models.company import Company
from models.dev import Dev
from models.freebie import Freebie

def seed_data():
    # Ensure the directory for the SQLite file exists
    os.makedirs(os.path.dirname("db/development.sqlite"), exist_ok=True)

    # Re-create all tables
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()

    # Create Companies
    apple     = Company(name="Apple", founding_year=1976)
    google    = Company(name="Google", founding_year=1998)
    microsoft = Company(name="Microsoft", founding_year=1975)

    # Create Devs
    alice = Dev(name="Alice")
    bob   = Dev(name="Bob")
    carol = Dev(name="Carol")

    session.add_all([apple, google, microsoft, alice, bob, carol])
    session.commit()

    # Create Freebies
    f1 = Freebie(item_name="Sticker Pack", value=5, dev=alice,   company=google)
    f2 = Freebie(item_name="T-shirt",       value=20, dev=bob,    company=apple)
    f3 = Freebie(item_name="Mug",           value=12, dev=carol,  company=microsoft)

    session.add_all([f1, f2, f3])
    session.commit()
    session.close()

    print("Seeding complete.")

if __name__ == '__main__':
    seed_data()
