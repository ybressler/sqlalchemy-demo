import datetime
from sqlalchemy import Column, Integer, String, DateTime

# Import your base tables
from database.models import Base, BaseTable


# ------------------------------------------------------------------------------

class Theatre(Base, BaseTable):
    """
    A table representing broadway theatres.
    """
    __tablename__ = 'theatre'


    id = Column(Integer, autoincrement=True, primary_key=True)

    # the basics
    theatre_name = Column(String(200), nullable=True)
    street_address = Column(String(300), nullable=True)
    capacity = Column(Integer, nullable=True, comment='How many seats are in this theater?')


    # date stuff
    date_opened = Column(DateTime, nullable=True)
    date_closed = Column(DateTime, nullable=True)
    date_demolished = Column(DateTime, nullable=True)




    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    # INTERNALLY MANAGED

    date_created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow, comment='internally managed')
    date_updated = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow, comment='internally managed')
