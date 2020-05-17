#!/bin/bash
docker build -t pulsetracker:0.1 .
docker run --rm -it pulsetracker:0.1 
