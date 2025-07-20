#!/bin/bash
docker build -t psutil-flask .
# Run the container
docker run -d -p 5276:5276 psutil-flask