

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///db/development.sqlite")
Session = sessionmaker(bind=engine)
Base = declarative_base()
