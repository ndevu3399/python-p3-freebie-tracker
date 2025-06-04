# models/company.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.freebie import Freebie
from models.dev import Dev

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer, nullable=False)

    # All Freebie objects this company has given:
    freebies = relationship("Freebie", back_populates="company", cascade="all, delete-orphan")

    # All Dev objects who have collected freebies from this company:
    devs = relationship("Dev", secondary="freebies", back_populates="companies", viewonly=True)

    @classmethod
    def oldest_company(cls, session):
        """
        Returns the Company instance with the earliest founding_year.
        Needs an active SQLAlchemy session passed in.
        """
        return session.query(cls).order_by(cls.founding_year.asc()).first()

    def give_freebie(self, session, dev, item_name, value):
        """
        Creates and persists a new Freebie belonging to this Company for the given Dev.
        - session: SQLAlchemy Session
        - dev: Dev instance
        - item_name: string
        - value: int
        """
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(new_freebie)
        session.commit()
        return new_freebie
