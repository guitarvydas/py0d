all: feedbackTest

feedbackTest:
	python3 fb.py

test:
	python3 test.py

clean:
	rm -f *~ junk*
