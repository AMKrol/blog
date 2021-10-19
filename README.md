# Blog

###### Training project

Aim of this project is to learn the basis of Django web framework.

## Features

- App allows to create, edit and delete the posts
- All posts is saved in database using PostgreSQL
- To create/edit/delete post user myst be loged in
- Operation on posts is allowed only for users with appropriate privigles

## Installation

After clone repository create virtual repository and install dependences:

```sh
cd blog/
python -m venv venv
source venv/bin/activate
pip install -r requrements.txt
```

Now the program can be run by following:
```sh
python manage.py runeserver
```

Enter to your favorite browser and go to:

```sh 
http://localhost:8000/
```

