# Makefile
.PHONY: install test build docker-build
install:
    pip install -r requirements.txt
test:
    pytest -q
build:
    python -m py_compile $(find app -name "*.py")
docker-build:
    docker build -t tasks-api:local .
