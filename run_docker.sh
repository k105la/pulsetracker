#!/bin/bash
docker build -t pulsetracker:0.1 .
docker run --rm -t -it pulsetracker:0.1 
