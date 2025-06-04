# models/dev.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.freebie import Freebie
from models.company import Company

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # All Freebie objects this dev has collected:
    freebies = relationship("Freebie", back_populates="dev", cascade="all, delete-orphan")

    # All Company objects this dev has collected freebies from:
    companies = relationship("Company", secondary="freebies", back_populates="devs", viewonly=True)

    def received_one(self, item_name):
        """
        Returns True if this Dev has any Freebie whose item_name matches the argument.
        """
        return any(f.item_name == item_name for f in self.freebies)

    def give_away(self, session, other_dev, freebie):
        """
        Transfers `freebie` from this Dev to other_dev if it currently belongs to this Dev.
        - session: SQLAlchemy Session
        - other_dev: Dev instance
        - freebie: Freebie instance
        """
        if freebie.dev_id == self.id:
            freebie.dev = other_dev
            session.add(freebie)
            session.commit()
            return True
        return False
