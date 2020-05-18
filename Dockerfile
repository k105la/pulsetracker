FROM ubuntu:18.04
COPY . ./pulsetracker
WORKDIR /pulsetracker
ENV PYTHONPATH /pulse/src
RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    sudo \ 
    libsm6 \
    libxext6 \
    python-pip \
    libxrender1 \
    libglib2.0-0 \
	python-setuptools \
	python3-setuptools
RUN make install 
RUN make
