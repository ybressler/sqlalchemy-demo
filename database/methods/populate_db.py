"""
We're going to add hardcoded values into our database so we have something
to experiment with. (This is cheating! But who cares...)
"""
import sys
import os

# This makes the file executable
if os.environ.get('PROJECT_PATH'):
    sys.path.append(os.environ.get('PROJECT_PATH'))



import datetime
from database.models import Theatre, Show, Person, Role, ShowsRolesLink
from database import session, DB_URI

to_year = lambda x: datetime.datetime(year=x, month=1, day=1)

# ------------------------------------------------------------------------------


theatre_records = [
    dict(
        theatre_name='Richard Rodgers Theatre',
        street_address='226 West 46th Street, New York, NY 10036',
        capacity=1_380,
        date_opened=to_year(1925)
    ),
    dict(
        theatre_name='Gershwin Theatre',
        street_address='222 West 51st Street New York, NY 10019',
        capacity=1_933,
        date_opened=to_year(1972)
    )
]


show_records = [
    dict(
        title='Hamilton',
        preview_date=datetime.datetime(year=2015, month=7, day=13),
        opening_date=datetime.datetime(year=2015, month=8, day=6),
        show_genre='Musical'

    ),
    dict(
        title='Wicked',
        preview_date=datetime.datetime(year=2003, month=10, day=8),
        opening_date=datetime.datetime(year=2003, month=10, day=30),
        show_genre='Musical'

    )
]


person_records = [
    # Some wicked people
    dict(
        first_name='Stephen',
        middle_name=None,
        last_name='Oremus',
        show='Wicked',
        role='Musical Director'
    ),
    dict(
        first_name='Joe',
        middle_name=None,
        last_name='Mantello',
        show='Wicked',
        role='Director'
    ),
    dict(
        first_name='Wayne',
        middle_name=None,
        last_name='Cilento',
        show='Wicked',
        role='Choreographer'
    ),
    dict(
        first_name='Charles',
        middle_name=None,
        last_name='LaPointe',
        show='Wicked',
        role='Associate Hair Design'
    ),

    # Some hamilton people
    dict(
        first_name='Alex',
        middle_name=None,
        last_name='Lacamoire',
        show='Hamilton',
        role='Musical Director'
    ),
    dict(
        first_name='Thomas',
        middle_name=None,
        last_name='Kail',
        show='Wicked',
        role='Director'
    ),
    dict(
        first_name='Stephanie',
        middle_name=None,
        last_name='Klemons',
        show='Wicked',
        role='Choreographer'
    ),

    dict(
        first_name='Charles',
        middle_name=None,
        last_name='LaPointe',
        show='Hamilton',
        role='Hair and Wig Design'
    )

]


# ------------------------------------------------------------------------------

def add_all_theatres(records=theatre_records):
    for rec in records:
        # look before you leap
        my_theatre = session.query(Theatre).filter(Theatre.theatre_name==rec['theatre_name']).first()
        if my_theatre:
            print(f'Theatre "{my_theatre.theatre_name}" already exists')
        else:
            my_theatre = Theatre(**rec)
            session.add(my_theatre)

    """
    Inspect the item you've just created:

        >> print(my_theatre.__dict__)

        {
            '_sa_instance_state': <sqlalchemy.orm.state.InstanceState at 0x7fae80837dc0>,
            'theatre_name': 'Gershwin Theatre',
            'street_address': '222 West 51st Street New York, NY 10019',
            'capacity': 1933,
            'date_opened': datetime.datetime(1972, 1, 1, 0, 0)
        }

    """

    # At the end, commit your session (or roll it back!)
    session.commit()




def add_all_shows(records=show_records):
    for rec in records:
        # look before you leap
        my_show = session.query(Show).filter(Show.title==rec['title']).first()
        if my_show:
            print(f'Show "{my_show.title}" already exists')
        else:
            my_show = Show(**rec)
            session.add(my_show)

    # At the end, commit your session (or roll it back!)
    session.commit()




def add_all_people(records=person_records):
    """
    This is not the best way to add these records to the db in any way, but it works
    and is kinda easy to read I hope...
    """
    for rec in records:

        # look before you leap
        my_person = session.query(Person)\
            .filter(
                Person.f_name==rec['first_name'],
                Person.m_name==rec['middle_name'],
                Person.l_name==rec['last_name'],
            )\
            .first()

        if my_person:
            print(f'Person "{my_person.full_name}" already exists')
        else:
            my_person = Person(
                f_name=rec['first_name'],
                m_name=rec['middle_name'],
                l_name=rec['last_name'],
                )
            session.add(my_person)

        # Now get the role that they're in
        my_role = session.query(Role).filter(Role.name==rec['role'].lower()).first()
        if my_role:
            print(f'Role "{my_role.name}" already exists')
        else:
            my_role = Role(name=rec['role'])
            session.add(my_role)


        # Commit here, since we need to look up by ids...
        session.commit()

        # Now add the record for the show they're in

        # get the show
        my_show = session.query(Show).filter_by(title=rec['show']).first()
        assert my_show

        work_experience = session.query(ShowsRolesLink)\
            .filter_by(
                person_id=my_person.id,
                role_id=my_role.id,
                show_id=my_show.id
            )\
            .first()
            
        if work_experience:
            print(f'Already have that work experience: person_id={my_person.id}; role_id={my_role.id}; show_id={my_show.id}')
        else:
            work_experience = ShowsRolesLink(
                person_id=my_person.id,
                role_id=my_role.id,
                show_id=my_show.id
            )
            print(work_experience)
            session.add(work_experience)
            session.commit()

    # All done!

#
#
if __name__ == '__main__':

    # Add em all!
    add_all_theatres()
    add_all_shows()
    add_all_people()
