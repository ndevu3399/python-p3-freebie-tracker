# models/freebie.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)

    dev_id = Column(Integer, ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)

    # RELATIONSHIPS
    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

    def print_details(self):
        """
        Returns: "<dev name> owns a <item_name> from <company name>"
        """
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
