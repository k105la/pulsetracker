FROM python:3.8
COPY . ./pulsetracker
WORKDIR /pulsetracker
ENV PYTHONPATH /pulse/src
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN make install 
RUN make
