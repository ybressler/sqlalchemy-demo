from sqlalchemy.ext.declarative import declarative_base
from database import metadata

# ------------------------------------------------------------------------------
"""
Create a base which will be used by all models.
This allows you to declare models without assigning them to the database transaction
until the are needed. This is a great way to avoid collisions with relationships.
"""
Base = declarative_base(metadata=metadata)
