tests:
	coverage erase
	coverage run manage.py test
	coverage report -m
