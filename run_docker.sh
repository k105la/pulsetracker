#!/bin/bash
docker build -t pulsetracker:0.1 .
docker run --rm -i -t pulsetracker:0.1 
