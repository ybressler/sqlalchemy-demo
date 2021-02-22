import sys
import os

# This makes the file executable
if os.environ.get('PROJECT_PATH'):
    sys.path.append(os.environ.get('PROJECT_PATH'))


from pathlib import Path
import datetime
from sqlalchemy_schemadisplay import create_schema_graph


# db stuff
from database import metadata


def create_db_ERD():

    # Create a path to store your ERD
    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime('%Y-%m-%d %H:%M:%S')
    save_path = Path(f'tmp/ERDs/Test Database ERD – {dt_now}.png')

    # Make the dir if you need to
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -

    graph = create_schema_graph(
        metadata=metadata,
        show_datatypes=True,
        show_indexes=True,
        rankdir='TB', # From left to right (instead of top to bottom)
        concentrate=True, # Don't try to join the relation lines together
        )

    graph.write_png(save_path)

    #  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -



if __name__ == '__main__':

    get_db_ERD()






#
