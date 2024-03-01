.PHONY: test install

test:
	poetry run pytest tests

install:
	poetry install

update lock:
	poetry lock --no-update