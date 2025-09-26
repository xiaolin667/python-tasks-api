.PHONY: install test build docker-build
install:
	pip install -r requirements.txt
test:
	pytest -q
build:
	python -m py_compile app/api.py
docker-build:
	docker build -t tasks-api:local .
