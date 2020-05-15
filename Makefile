SRC_CODE='./src/heartrate.py'
TEST_TIME='./tests/test_time.py'
TEST_GRAY='./tests/test_gray.py'

all:
	sudo python setup.py install

install:
	pip install -r requirements.txt

test:
	python ${TEST_TIME}
	python ${TEST_GRAY}

lint:
	pylint ${SRC_CODE} --extension-pkg-whitelist=cv2

clean:
	rm -rf ./images/
	rm -rf ./*/images/
