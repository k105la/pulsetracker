#!/bin/bash
docker build -t heartrate:0.1 .
docker run --rm -it heartrate:0.1 
