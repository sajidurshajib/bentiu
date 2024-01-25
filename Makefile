create_env: 
	@python3 -m venv env

activate_env:
	@. env/bin/activate

install: activate_env
	@pip3 install -r requirements.txt

start: activate_env
	@python3 university/manage.py runserver

start-dev:
	@python3 university/manage.py livereload