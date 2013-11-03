#FROM ubuntu:quantal
FROM boxcar/raring

RUN apt-get -y update
RUN apt-get -y install build-essential curl git
RUN apt-get -y install python python-virtualenv python-dev
RUN apt-get -y install libxml2-dev libxslt-dev
