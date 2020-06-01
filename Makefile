SRC_CODE='./src/pulse.py'
TEST_TIME='./tests/test_time.py'
TEST_GRAY='./tests/test_gray.py'
TEST_PEAKS='./tests/test_peaks.py'
TEST_SIGNAL='./tests/test_sigdiff.py'
TEST_VARI='./tests/test_variances.py'
TEST_BPM='./tests/test_bpm.py'


all:
	pip3 install -e .

install:
	pip3 install -r requirements.txt

test:
	python3 ${TEST_TIME}
	python3 ${TEST_GRAY}
	python3 ${TEST_SIGNAL}
	python3 ${TEST_VARI}
	python3 ${TEST_VARI}
	python3 ${TEST_BPM}
	rm -rf ./images/

lint:
	flake8 --ignore=E722,E501,W291,W293 src/pulse.py
	pylint --disable=trailing-whitespace,superfluous-parens,missing-docstring,bare-except,len-as-condition --extension-pkg-whitelist=cv2 --max-line-length=120 src/	

clean:
	rm -rf ./images/
	rm -rf ./*/images/
