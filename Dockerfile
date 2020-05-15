FROM ubuntu:18.04
COPY . ./heartrate
WORKDIR /heartrate
ENV PYTHONPATH /heartrate/src
RUN apt-get update && apt-get install -y --no-install-recommends \
    make \
    sudo \ 
    libsm6 \
    libxext6 \
    python-pip \
    libxrender1 \
    libglib2.0-0
RUN make install 
