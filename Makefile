lint:
	./tools/lint.sh
test: 
	./tools/runtests.sh
validate: lint test

