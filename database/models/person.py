import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property

# Import your base tables
from database.models import Base, BaseTable


# --------------------------------------------------------------------------------


class Person(Base, BaseTable):
    """
    A table representing a person. (These are people who've work on a Broadway show.)
    """
    __tablename__ = "person"

    id = Column(Integer, autoincrement=True, primary_key=True)

    # Break a name down to its pieces...
    f_name = Column(String(40), nullable=True, unique=False)
    m_name = Column(String(40), nullable=True, unique=False)
    l_name = Column(String(40), nullable=True, unique=False)

    @hybrid_property
    def full_name(self):
        """Put the name together..."""
        return " ".join(list(filter(None, [self.f_name, self.m_name, self.l_name])))

    # --------------------------------------------------------------------------

    # one to many
    roles = relationship('Role', secondary='shows_roles_link', backref=backref('person', lazy='dynamic'), passive_deletes=True)
    shows = relationship('Show', secondary='shows_roles_link', backref=backref('person', lazy='dynamic'), passive_deletes=True)

    
    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -
    # INTERNALLY MANAGED

    date_created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow, comment='internally managed')
    date_updated = Column(DateTime, nullable=True, onupdate=datetime.datetime.utcnow, comment='internally managed')
