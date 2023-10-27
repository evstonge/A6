all: style-check type-check unittest test fix-style kattis
	@echo "All done..."

unittest:
	pytest -v test_hvertskalmaeta.py
	
test:
	@cat 1.in | python hvertskalmaeta.py | diff - 1.ans
	@cat 2.in | python hvertskalmaeta.py | diff - 2.ans
	@echo "All local test passed..."

style-check:
	flake8 .

type-check:
	mypy --strict .

fix-style:
	autopep8 --in-place --aggressive --aggressive hvertskalmaeta.py

kattis:
	@kattis -f hvertskalmaeta.py