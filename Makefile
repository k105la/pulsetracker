SRC_CODE='./src/pulse.py'
TEST_FOLDER='./tests/'
TEST_TIME='./tests/test_time.py'
TEST_GRAY='./tests/test_gray.py'
TEST_PEAKS='./tests/test_peaks.py'
TEST_SIGNAL='./tests/test_sigdiff.py'
TEST_VARI='./tests/test_variances.py'


all:
	pip install -e .

install:
	pip install -r requirements.txt

test:
	python ${TEST_TIME}
	python ${TEST_GRAY}
	python ${TEST_PEAKS}
	python ${TEST_VARI}
	python ${TEST_SIGNAL}
	rm -rf ./images/

lint:
	pylint ${SRC_CODE} --extension-pkg-whitelist=cv2
	pylint ${TEST_TIME}
	pylint ${TEST_GRAY}
	pylint ${TEST_PEAKS}
	pylint ${TEST_VARI}
	pylint ${TEST_SIGNAL}
	
clean:
	rm -rf ./images/
	rm -rf ./*/images/
