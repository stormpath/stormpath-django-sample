run:
	python manage.py syncdb
	python manage.py runserver

install:
	pip install -r requirements.txt
