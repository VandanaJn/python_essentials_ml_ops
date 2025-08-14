install:
	python -m pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=. --cov-config=.coveragerc &&\
	python -m pytest --nbval-lax notebooks
	

debug:
	python -m pytest -vv --pdb	#Debugger is invoked

format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test format
