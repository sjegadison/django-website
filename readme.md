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
Createds btre folder on current directory

# python manage.py help
Managing Python Environment












