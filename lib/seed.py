#!/usr/bin/env python3



from db_setup import Base, engine, session
from models import Dev, Company


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


alice = Dev(name="Alice")
bob   = Dev(name="Bob")

hackathon_hub = Company(name="HackathonHub", founding_year=2010)
dev_swag_co   = Company(name="DevSwagCo",   founding_year=2015)

session.add_all([alice, bob, hackathon_hub, dev_swag_co])
session.commit()


hackathon_hub.give_freebie(alice, "Sticker Pack",   1)
hackathon_hub.give_freebie(bob,   "Laptop Sleeve", 25)
dev_swag_co.give_freebie(alice,   "T-Shirt",       20)
dev_swag_co.give_freebie(bob,     "Water Bottle",  10)

print("✅ Seeding complete!")
