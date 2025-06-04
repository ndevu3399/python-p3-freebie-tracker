# migrations/003_create_freebies.py

from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)

    dev_id = Column(Integer, ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
