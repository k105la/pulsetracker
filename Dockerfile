FROM python:3
COPY . ./pulsetracker
WORKDIR /pulsetracker
ENV PYTHONPATH /pulse/src
RUN make install 
RUN make
