.PHONY: env run migrations migrate shell

venv:
	python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

run: 
	python manage.py runserver 8080

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

shell:
	python manage.py shell_plus --ipython