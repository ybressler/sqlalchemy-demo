import sys
import os

# This makes the file executable
if os.environ.get('PROJECT_PATH'):
    sys.path.append(os.environ.get('PROJECT_PATH'))


from database.models import Theatre, Show, Person, Role, ShowsRolesLink
from database import session, DB_URI




# ------------------------------------------------------------------------------
def DELETE_EVERYTHING():
    """If you want to wipe your db clean"""

    for cls in [ShowsRolesLink, Show, Theatre, Person, Role]:
        session.query(cls).delete()

    # Commit at the end of the loop
    session.commit()



if __name__ == '__main__':
    uh_oh = input('Are you sure you want to remove all records from your database?')

    if uh_oh and uh_oh.lower() in ['t', 'True','y', 'yes']:
        uh_oh = True
    else:
        uh_oh = False

    # Add em all!
    if uh_oh:
        DELETE_EVERYTHING()
        print('Your database is now as pure and clean as a baby')

    else:
        print('Okay, we won\'t remove values...')
