#!/bin/bash
docker build -t pulsetracker:0.1 .
docker run --rm -i pulsetracker:0.1 sh -c "make test"
