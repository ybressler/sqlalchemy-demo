import sys
import os

# This makes the file executable
if os.environ.get('PROJECT_PATH'):
    sys.path.append(os.environ.get('PROJECT_PATH'))


from database.models import Theatre, Show, Person, Role, ShowsRolesLink
from database import session, DB_URI

show_a_id = session.query(Show.id).filter_by(title='Hamilton').first()
show_b_id = session.query(Show.id).filter_by(title='Wicked').first()

session.query(ShowsRolesLink).all()

#
# my_people = session.query(ShowsRolesLink)\
#     .filter(
#         ShowsRolesLink.show_id.in_(show_a_id.id, show_b_id.id)
#     )\
#     .all()
#
# my_people
#
# res = session.query(ShowsRolesLink).all()
#
#

# ------------------------------------------------------------------------------
def people_work_on_both_shows(show_name_a, show_name_b):
    """
    Which people worked on 2 shows?

    (Didn't get around to finiing this.)
    """

    show_a_id = session.query(Show.id).filter_by(title=show_name_a).subquery()
    show_b_id = session.query(Show.id).filter_by(title=show_name_b).subquery()

    people_show_a = session.query(ShowsRolesLink.person_id)\
        .filter(
            ShowsRolesLink.show_id==show_a_id
        )\
        .all()

    people_show_b = session.query(ShowsRolesLink.person_id)\
        .filter(
            ShowsRolesLink.show_id==show_b_id
        )\
        .all()

    people_show_a = set(x[0] for x in people_show_a)
    people_show_b = set(x[0] for x in people_show_b)

    shared_people_ids = people_show_a.intersection(people_show_b)

    shared_people = session.query(Person).filter(Person.id.in_(shared_people_ids)).all()
    return shared_people




if __name__ == '__main__':

    shared_people = people_work_on_both_shows('Hamilton', 'Wicked')

    print(f'There are {len(shared_people):,} people who have worked on both shows;\nTheir names are:', *[x.])
