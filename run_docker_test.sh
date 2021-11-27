#!/bin/bash
docker build -t pulsetracker:latest .
docker run --rm -i pulsetracker:latest sh -c "make test"
