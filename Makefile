test:
	python -m pytest --cov-config=.coveragerc --cov-report html --cov=.


run:	
	uvicorn app.main.main:app --reload
