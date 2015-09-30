lint:
    python bin/linter.py

install:
    pip install -r requirements.txt

test:
    cd tests/ && nosetests