tests:
	coverage erase
	coverage run manage.py test
	coverage report -m

style:
	ruff format spendings/ yaba/ manage.py

