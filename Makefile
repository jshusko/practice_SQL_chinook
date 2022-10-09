setup:
	pip install -r package-list.txt
run:
	python chinook-queries.py; cat chinook-queries.sql | sqlite3 chinook.db
				
test:
	python chinook-queries.py; cat chinook-queries.sql | sqlite3 chinook.db; python test_chinook-queries.py
