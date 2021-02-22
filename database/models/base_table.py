import os
import json
import datetime

# sqlalchemy stuff
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import class_mapper, ColumnProperty
from sqlalchemy.exc import IntegrityError

# db stuff
from database import session


# ------------------------------------------------------------------------------


class BaseTable():
    """
    Base class for all objects in a table.

    Some handy baseline functions which will make your life much easier.
    """

    # --------------------------------------------------------------------------
    # STRING METHODS

    # Define string methods...
    def __data__(self):
        data = {x: getattr(self, x) for x in self.__mapper__.columns.keys()}
        return data

    def __str__(self):
        data = self.__data__()
        return json.dumps(data, default=str)


    # --------------------------------------------------------------------------
    # DATABASE METHODS


    # Lookup by attr
    @classmethod
    def get_by_attr(self, attr, value):
        """
        Get the an entity based on the first match of a give attribute.

        Ex: get_by_attr('full_name','Brad Pitt')
            returns --> get first instance of Brad Pitt (or None)
        """

        return self.session.query(self).filter(getattr(self, attr)==value).first()


    # --------------------------------------------------------------------------
