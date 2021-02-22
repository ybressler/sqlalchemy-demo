# SQLAlchemy Demo
The following repo is a demo for how to create a manage a database using sqlalchemy.

## Before you get started
You'll need a database configured to your local machine. I'd suggest using MySQL or Postgres.
Both are free and are easy to manage. For the purpose of this demo, it does not matter
which database you choose to use.

## Getting started
_The following is written for unix machines..._
1. Launch a new (and empty) database from your local machine:
* Here's a video tutorial how to create a database on your machine: https://youtu.be/LXKTQWoQAj8
* I recommend using [Postgres.app](https://postgresapp.com/)


2. Download this repository to your local machine:
```
git clone https://github.com/ybressler/sqlalchemy-demo.git
```

3. Create a virtual environment and activate it. Then, install the requirements:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
_You're now ready to begin!_

4. Store your DB_URI as an environment variables _or_ update the value in the code.
<br>_For example, following default values:_
```
export DB_URI='postgresql://postgres:@localhost:5432/postgres'
```
For more info as to what's going on here, give this a read: FOO


5. Export the full path of your current project the environment variable `PROJECT_PATH`:
```
export PROJECT_PATH=$(pwd)
```
_This will allow you to execute nested files as executables, without dealing with
issues like relative imports. In a production setting, your modules will likely be
imported properly and executed from a central orchestrator (such as a web app)._

6. Do this
