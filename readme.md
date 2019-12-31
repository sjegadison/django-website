# Create Virual Environment
pip3 freeze
python3 -m venv ./venv
pip3 freeze

# Activate/ DeActivate/ Activate Virual Environment
(base) Sivaguru-MBP:btre_project siva$ source ./venv/bin/activate
(venv) (base) Sivaguru-MBP:btre_project siva$ python --version
Python 3.8.0
(venv) (base) Sivaguru-MBP:btre_project siva$ deactivate
(base) Sivaguru-MBP:btre_project siva$ python --version
Python 2.7.16
(base) Sivaguru-MBP:btre_project siva$ source ./venv/bin/activate
(venv) (base) Sivaguru-MBP:btre_project siva$ pip3 freeze
(venv) (base) Sivaguru-MBP:btre_project siva$ 

# pip install django (venv)

# pip freeze (venv)
asgiref==3.2.3
Django==3.0.1
pytz==2019.3
sqlparse==0.3.0

# django-admin help 

# django-admin startproject btre .
Created btre folder on current directory

# python manage.py help
Managing Python Environment

# git init ( gitignore.io - create .gitignore and copy the content for django)
(venv) (base) Sivaguru-MBP:btre_project siva$ git init
Initialized empty Git repository in /Users/siva/python/PythonDev_Deploy/btre_project/.git/
(venv) (base) Sivaguru-MBP:btre_project siva$ 

(venv) (base) Sivaguru-MBP:btre_project siva$ git add .  && git commit -m 'Initial Commit'
[master (root-commit) 37353cc] Initial Commit
 9 files changed, 362 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 .vscode/settings.json
 create mode 100644 btre/__init__.py
 create mode 100644 btre/asgi.py
 create mode 100644 btre/settings.py
 create mode 100644 btre/urls.py
 create mode 100644 btre/wsgi.py
 create mode 100755 manage.py
 create mode 100644 readme.md

# Run Django Server 
python manage.py runserver

# create pages app
python manage.py startapp pages

# settings.py of folder btre
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
where PagesConfig from apps.py of Pages App Folder

# views.py of Pages App Folder
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello World</h1>')

# Create urls.py in Pages App Folder

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
]

# urls.py of folder btre - Add Line

    path('',include('pages.urls')), in urlpatterns = [

# Create static Folder ion btre project folder and create static folder and copy static files
## Then run , in settings.py

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT =  os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'btre/static')
]

### then run, 
python manage.py collectstatic

(venv) (base) Sivaguru-MBP:btre_project siva$ python manage.py collectstatic

161 static files copied to '/Users/siva/python/PythonDev_Deploy/btre_project/static'.
(venv) (base) Sivaguru-MBP:btre_project siva$ 













