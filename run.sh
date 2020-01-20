#!/bin/bash

docker build -t avanetix_qws -f config/avanetix_qws.Dockerfile .
docker run -it -v ${PWD}:/usr/local/bin/avanetix_qws -p 8888:8888 avanetix_qws
