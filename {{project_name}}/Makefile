SHELL=/bin/bash

.PHONY: init npm run dev migrations migrate shell

init:
	cp .env.example .env && \
	git init && \
	python3 -m venv .venv && \
	source .venv/bin/activate && \
	pip install -r requirements.txt && \
	npm install

npm:
	npm run dev
run: 
	python manage.py runserver 8000
dev:
	make -j 2 npm run
migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

shell:
	python manage.py shell_plus --ipython
