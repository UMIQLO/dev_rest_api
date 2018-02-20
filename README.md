# MP_DEV
MP_DEV
## Usage
    python -m venv python_venv
    python_venv\Scripts\activate
	pip install django
	pip install mysqlclient
    pip install djangorestframework
## django manage.py Usage
	python manage.py makemigrations <app name>
	python manage.py migrate <app name> --database=<db setting name>
	python manage.py runserver