import datetime

# sqlalchemy stuff
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy


# Import your base tables
from database.models import Base, BaseTable


# ------------------------------------------------------------------------------

class Show(Base, BaseTable):
    """
    A table representing a broadway show.
    """
    __tablename__ = 'show'

    # I like to explicitly state autoincrement, better than implicit
    id = Column(Integer, autoincrement=True, primary_key=True)

    # the basics
    title = Column(String(200), nullable=True, comment='This is the name of the show.')
    preview_date = Column(DateTime, nullable=True)
    opening_date = Column(DateTime, nullable=True)
    closing_date = Column(DateTime, nullable=True)


    # types – use enums
    show_genre = Column(String(20), nullable=True)


    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    # RELATIONSHIPS
    theatre_id = Column(Integer, ForeignKey('theatre.id'), nullable=True, index=True, comment='Which theatre did this show perform in?')

    # Creating a relationship is *this* easy
    theatre = relationship('Theatre', backref='show')
    theatre_name = association_proxy('theatre', 'theatre_name')



    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    # INTERNALLY MANAGED

    date_created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow, comment='internally managed')
    date_updated = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow, comment='internally managed')


    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    def __repr__(self):
        return f"{self.id}: {self.title} ({self.year})"
