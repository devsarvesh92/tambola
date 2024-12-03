install:
	pdm install

format:
	pdm run black .
	pdm run ruff check . --fix

test:
	pdm run pytest

run-test:
	pdm run pytest -k ${test}