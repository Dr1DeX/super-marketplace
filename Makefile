install:
	poetry add ${LIB}

remove:
	poetry remove ${LIB}

update:
	poetry update ${LIB}

run:
	poetry run uvicorn app.main:app --host localhost --port 8000 --reload --env-file ${ENV}

migrate-create:
	alembic revision --autogenerate -m ${MIGRATION}

migrate-apply:
	alembic upgrade head