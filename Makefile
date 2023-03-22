all: test

test:
	python3 test.py

clean:
	rm -f *~ junk*
