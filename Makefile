venv_path = .venv
venv_bin = $(venv_path)/bin/
req_path = requirements/

#env.setup: @ Installs environment dependencies, creates virtual envi MLRD-63 Feature: ronment and installs dev python packages

env.setup: e.install-apps e.create-virtualenv env.install-python-dependencies

#env.delete : @ Deletes the virtual environment created
env.delete:
	rm -rf $(venv_path)

e.install-apps:
	brew install pyenv
	pyenv install 3.6.8
	python3 -m pip install virtualenv

e.create-virtualenv:
	python3 -m virtualenv -p ~/.pyenv/versions/3.6.8/bin/python $(venv_path)


#env.install-python-dependencies: @ Installs development python dependencies
env.install-python-dependencies:
	$(venv_path)/bin/pip install -r $(req_path)requirements.txt

#env.update: @ Updates all python dependencies
env.update: e.update env.install-python-dependencies

e.update:
	$(venv_bin)pip-compile -r --no-index requirements.in --max-rounds=20
	$(venv_bin)pip-compile -r --no-index requirements-dev.in --max-rounds=20
