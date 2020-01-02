# Clear Browser Cache - Cmd + Shift + R (Mac) - Shift + F5 (Windows)
# clear in terminal window Mac shortcut - Cmd L
# Less Secure Apps : https://myaccount.google.com/lesssecureapps
# Deployment Instruction Link
https://gist.github.com/bradtraversy/cfa565b879ff1458dba08f423cb01d71

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

# https://postgresapp.com/downloads.html
# https://www.postgresql.org/ftp/pgadmin/pgadmin4/v4.16/macos/

# Postgres Console
postgres=# \password postgres
Enter new password: Postgres
Enter it again: Postgres
postgres=# CREATE DATABASE btredb OWNER postgres;
CREATE DATABASE
postgres=# \l --- List databases

# pgAdmin Pwd : PGAdmin

# which pg_config
/Applications/Postgres.app/Contents/Versions/10/bin/pg_config

Add this to .bash_profile PATH 

nano .bash_profile
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/10/bin

# settings.py of btre project
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btredb',
        'USER': 'postgres',
        'PASSWORD': 'Postgres',
        'HOST': 'localhost'
    }
}

# Migrate
python manage.py migrate 

## You can also use
python manage.py migrate listings
python manage.py migrate realtors

# Create Models for Listing and Realtors ( models.py)
pip install pillow -- To use ImageField

# Run - python manage.py makemigrations 
It will create Table Postgres Source Code in Migration Folder

# To show SQl
python manage.py sqlmigrate listings 0001

# Migrate models

## python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, listings, realtors, sessions
Running migrations:
  Applying realtors.0001_initial... OK
  Applying listings.0001_initial... OK

# Create Admin Superuser
python manage.py createsuperuser
User ID: siva
Password  : Admin

# To store Images

## settings.py of btre Project Folder

# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

## urls.py of btre Project Folder

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('pages.urls')),
    path('listings/',include('listings.urls')),
    path('admin/', admin.site.urls),

## add line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin Console UI Enhancements
Create a folder admin below templates
Create a file named base_site.html and write

{% extends 'admin/base.html' %}
{% load static %}

{% block branding %}
<h1 id="head">
    <img src="{% static 'img/logo.png' %}" alt="BT Real Estate" class="brand_img" height=50 width=80>
    Admin Area
</h1>
{% endblock %}

# Css customization of Admin Website
In btre project folder under sttic folder,
create admin.css and add styles
In file base_site.html add 


{% block extrastyle %}
    <link rel="stylesheet" href="{% static 'css/admin.css' %}">
{% endblock %}

# Custon Clickable / Search / Filter / Editable  Columns of Listings
In admin.py of listings folder

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published','price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter= ('realtor','price')
    list_editable=('is_published',)
    search_fields=('title','description','address','city','state','zipcode','price')
    list_per_page=25

admin.site.register(Listing,ListingAdmin)

# Custon Clickable / Search / Filter / Editable  Columns of Realtors
In admin.py of realtors folder

# Fetch :istings from DB

In listings -> views.py

from.models import Listing

def index(request):
    listingsData = Listing.objects.all()
    context = {
        'listings': listingsData
    }
    return render(request, 'listings/listings.html', context)

# git add . ; git commit -m "Message" ; git push -u origin master
## for VS Code Intellisense to work :
Ref : https://stackoverflow.com/questions/45135263/class-has-no-objects-member

pip install pylint-django

Then in Visual Studio Code goto: User Settings (Ctrl + , or File > Preferences > Settings if available ) Put in the following (please note the curly braces which are required for custom user settings in VSC):

    "python.linting.pylintArgs": [
        "--load-plugins", "pylint_django",
        "--errors-only"
    ],
(or) 

Add .pylintrc file in the base folder -- refer to alsouse.pylintrc

# Adding Dynamic Listings
Look for code in templates -> listings -> listings.html

# accounts and Authentication
python manage.py startapp accounts



 











