install:
	poetry add ${LIB}

remove:
	poetry remove ${LIB}

update:
	poetry update ${LIB}

run:
	poetry run uviicorn --host localhost --port 8000 --reload