# Django/MySQL/Graphql/Strawberry Backend Setup

## Set-up Virtual Environment for Backend
### Install virtualenv
```
pip install virtualenv
virtualenv venv
```
### Activate virtualenv
```
source venv/bin/activate
. venv/bin/activate
```

## Set-up Django for Backend
### Install django
```
pip install django
```
## Create Base Template for Django
  - django-admin startproject (name of project) .
  - the . removes the double nested folder
```
django-admin startproject django_server .
```
- Folder structure should look like this
```
django_server/
  manage.py
  django_server/
      __init__.py
      settings.py
      urls.py
      asgi.py
      wsgi.py
```

## Create Base File/Create Api File
- python manage.py startapp {name}
```
python manage.py startapp api
```
- add to settings.py
###

## Inital run of templated database migrations and start the development server:
  - We will need to run again after we add our data
```
(venv) $ cd django_server
(venv) django_server $ python manage.py migrate
(venv) django_server $ python manage.py runserver
```

## Django should be up
- Now, visit http://127.0.0.1:8000/

## Freeze your pip dependencies
- Now, anyone who checks out your code (including your deployment script) can run pip install -r requirements.txt to replicate your environment.
```
pip freeze > requirements.txt
```

# SKIP FOR NOW

## Public Libraries (Skip)
```
(venv) venv $ pip install isort flake8 black pre-commit seed-isort-config flake8-bugbear
(venv) venv $ pip freeze > requirements.txt
(venv) venv $ git init
```

## Create a Git Ignore
- In .gitignore
```
__pycache__/
db.sqlite3
```

## Add ``.pre-commit-config.yaml`` file at the project root (Skip)
```
repos:
  - repo: https://github.com/psf/black
    rev: 19.10b0
    hooks:
      - id: black
        language_version: python3.7
- repo: https://github.com/asottile/seed-isort-config
    rev: v2.1.1
    hooks:
      - id: seed-isort-config
- repo: https://github.com/timothycrosley/isort
    rev: 4.3.21
    hooks:
      - id: isort
- repo: https://gitlab.com/pycqa/flake8
    rev: 3.8.1
    hooks:
      - id: flake8
        additional_dependencies: [flake8-bugbear]
```

## Add ``.flake8`` at the project root (Skip)
- Create, .flake8 file
```
[flake8]
select = C,E,F,W,B,B950
ignore = E203, E501, W503
max-line-length = 90
exclude = .git, __pycache__
```

## Install Pre-commit (Skip)
    - from virtualenv and backend
```
pre-commit install
pre-commit run --all-files
```

## Setting up Strawberry with Grapghql
```
pip install 'strawberry-graphql[debug-server]'

pip freeze > requirements.txt
```
# (End of Skip - Start Here)

<!-- ## WebSockets
- To support graphql Subscriptions over WebSockets you need to provide a WebSocket enabled server.
- The debug server can be made to support WebSockets with these commands
- Might be installed by Django**
```

pip install 'uvicorn[standard]'
``` -->
## Setting Up MySQL Database

```
pip install mysqlclient
```

## Open MySQL Client or use MySQL Workbench
- mysql -u name -p ***
```
CREATE DATABASE DB_name;
use DB_name;
show tables;
```

## Setup Backend
```
DATABASES = {
    'default": {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB-name',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'DB-User',
        'PASSWORD': 'DB-Password',

    }
}

python manage.py makemigrations
python manage.py migrate
```

## Django SUPERUSER
```
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
python manage.py runserver
```

## Django Models
Django add "s" to Model names
- https://docs.djangoproject.com/en/4.0/ref/models/fields/
```py
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    sage_id = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)

    ## Used to reference in admin portal
    def __str__(self):
        return {self.first_name, self.last_name}
python manage.py makemigrations
python manage.py migrate
```

## More Examples
```
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField(default=2022)
    imdb_score = models.FloatField()
    poster_url = models.TextField()
    director = models.ForeignKey('Director', on_delete=models.PROTECT, null=True) or ('Director', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title + ' - ' + str(self.year)

class Director (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    movies = models.ManyToManyField(Movie, related_name='directors')
```

## app.py
- movies might need to change to show proper file configs we are not using the double nested
```
class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies.api'
```

## Register with Admin Area in Admin.py
```
from django.contrib import admin
from .models import User

admin.site.register(User)
```

## Calling Model Data
```py
from .models import User
#example
all_users = User.objects.all

## to strawberry example
import strawberry

from user.models import User
from . import types

@strawberry.type
class Get_User_Query:
    @strawberry.field
    def user(self, info, id: str) -> types.[User]:
        user = User.objects.find(id)
        if user:
            return user
        else:
            return {"error": "User not found"}
    # Need to workout how this acutally gets shaped

    # Basic Example
    @strawberry.type
    class Query:
    user: List[User] = strawberry.django.field()

schema = strawberry.Schema(query=Query)
## this will be imported to the main query
```
The query from the client side would be like
```
query {
  user(id: 4) {
    name
    ...
  }
}
```
# from . import types
```
# types.py
import strawberry
from strawberry.django import auto
from typing import List
from . import models

@strawberry.django.type(models.Users)
class User:
    id:auto
    first_name : str
    last_name : str
    email : str
    password : str
    address : str
    sage_id : str
    is_admin : boolean
```


## Example Farm
https://github.com/pythonitalia/pycon



## url.py
```
from django.urls import path

from strawberry.django.views import GraphQLView

from api.schema import schema

urlpatterns = [
    path("graphql/", GraphQLView.as_view(schema=schema)),
]
```
https://jaydenwindle.com/writing/strawberry-graphql-part-1/
## INSTALLED_APPS in settings.py
- strawberry.django
```
INSTALLED_APPS = [
    "corsheaders",
    "django_celery_beat",
    "django_celery_results",
    "django_extensions",
    ...
    'strawberry.django',
]

```

## Create schema.py and Basic Schema Example
```
import typing
import strawberry

@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class Query:
    books: typing.List[Book]
```

```Create TypeDef
def get_books():
    return [
        Book(
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
        ),
    ]


```
## Create Resolvers Files
@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


##


## Add schema.py and Run it?

```
schema = strawberry.Schema(query=Query)
```

- Run this in bash
```bash
strawberry server schema
```


## What I want
```
mybackend/
  manage.py
  mybackend/
      __init__.py
      settings.py
      urls.py
      asgi.py
      wsgi.py
  graphqlapi/
    resolvers/
        Query.py
        Mutation.py
        Other.py
    schema.py
```


# File Structure

## For the Main, schema.py

- https://github.com/pythonitalia/pycon/blob/5fd6198975da69c3372cd1ab1f0985fd37f6caba/backend/api/schema.py
```
import strawberry

from api.users.types import User

from .blog.schema import BlogQuery
from .conferences.schema import ConferenceQuery
from .grants.mutations import GrantsMutations
from .newsletters.schema import NewsletterMutations
from .orders.mutations import OrdersMutations
from .orders.query import OrdersQuery
from .pages.schema import PagesQuery
from .schedule.mutations import ScheduleMutations
from .submissions.mutations import SubmissionsMutations
from .submissions.schema import SubmissionsQuery
from .users.schema import CountryQuery
from .voting.mutations import VotesMutations


@strawberry.type
class Query(
    ConferenceQuery,
    BlogQuery,
    SubmissionsQuery,
    PagesQuery,
    CountryQuery,
    OrdersQuery,
): pass


@strawberry.type
class Mutation(
    SubmissionsMutations,
    VotesMutations,
    OrdersMutations,
    GrantsMutations,
    NewsletterMutations,
    ScheduleMutations,
): pass


schema = strawberry.federation.Schema(query=Query, mutation=Mutation, types=[User])
```


## Using Graphene Errors
- ImportError: cannot import name 'force_text' from 'django.utils.encoding'

https://stackoverflow.com/questions/70524028/importerror-cannot-import-name-force-text-from-django-utils-encoding-usr?msclkid=ec5c8150aad511ec865c6a96f67b0b09


## Dockerizing our Django App

Create a Dockerfile on the root directory of the project.
```
# /Dockerfile
FROM python:3.9
# PYTHONUNBUFFERED variable is used for non-buffered stdout
ENV PYTHONUNBUFFERED=1
# update the packages
RUN apt update -y && apt upgrade -y

# changing our working directory to be /usr/src
WORKDIR /usr/src/

# copying and installing python requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copying the whole django application
COPY xkcd_app/ .

# exposing our django port: 8000
EXPOSE 8000

# serving django with gunicorn on port 8000 (1 worker, timeout of 60 secs)
CMD [gunicorn, --bind, 0.0.0.0:8000, --workers, 1, --timeout, 60, xkcd_app.wsgi]
```

- <b>Noted Issue: gunicorn not found</b>

## Testing the Docker Image
Let's build and run our docker image.
```
# build the image with the latest tag
docker build -t xkcd:latest .

# run the image with port mapping 8000 to 8000
docker run -p 8000:8000 xkcd:latest

# output should look something like this.
# ... [1] [INFO] Starting gunicorn 20.1.0
# ... [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
# ... [1] [INFO] Using worker: sync
# ... [8] [INFO] Booting worker with pid: 8
```


## Graphql with Graphene
- default output is camelCase
```
query{
    allMovies{
        title
    }
}
- even though "all_movies" is was the name
```

## Make Master Schema
- in schema.py in our root
```
import graphene

class Query(graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    pass


query = graphene.Schema(query=Query, mutation=Mutation)

```
## In settings.py
```
allows this to be master schema (notes to come )
GRAPHENE = {
    'SCHEMA': 'movies.schema.schema'
}


```

## Queries in Graphene
- Kwargs are your inputs!!!
```
query {
  movie(id:1){
    id
    imdbScore
    title
    posterUrl
  }
}

def resolve_movie(self, info, **kwargs):
    print(kwargs) ==> {'id': 1}
    id = kwargs.get('id')

    if id is not None:
        return Movie.objects.get(pk=id)

    return None
```

## Custom Queries in Type
```
class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

    # custom queries (movie_age)
    movie_age = graphene.String()

    def resolve_movie_age(self, info):
        if self.year < 2022:
            return "Old Movie"
        else:
            return "New Movie"
```
### Can be passed in query
- This is same as having some standard output on the Movie Type
```
query {
  allMovies(year:2022, imdbScore:5){
    id
    imdbScore
    title
    year
    movieAge
  }
```

### Multiple Queries (Alias + Fragments)
- firstAllMovies: + secondAllMovies: are Alias.
- Does this mean we need to Normalize?
```
query {
  firstAllMovies: allMovies(year:2022, imdbScore:5){
    id
    imdbScore
    title
    year
    movieAge
  }
  secondAllMovies: allMovies(year:2022, imdbScore:5){
    id
    imdbScore
    title
    year
    movieAge
  }
```
### Fragment - the above is pretty tedious
```
query {
  firstAllMovies: allMovies(year:2022, imdbScore:5){
    MovieData...
  }
  secondAllMovies: allMovies(year:2022, imdbScore:5){
    MovieData...
  }

fragment on MovieData on MovieType {
    id
    title
    director{
        first_name
    }
}
```
### Names, Variables, Directives
```
query MoviesAndDirectors($id: Int){
    movie(id:$id){
        id
        title
        year
        director{
            first_name
        }
    }
}

# Might need camelCase
query JustDirectors($first_name: String, $last_name: String){
    director(first_name:$first_name, last_name:$last_name, ){
        first_name
        }
    }
}
```

#### Directives
```
query MoviesAndDirectors($id: Int, $showdirector: Boolean=false){
    movie(id:$id){
        id
        title
        year
        director @includes(if: $showdirector) {
            first_name
        }
    }
}

```

## Mutations! 
