#FROM ubuntu:quantal
#FROM boxcar/raring
FROM yebyen/saucy

RUN apt-get -y update
RUN apt-get -y install build-essential curl git
RUN apt-get -y install libz-dev
RUN apt-get -y install libxml2-dev libxslt-dev
RUN apt-get -y install python python-dev

RUN curl -O https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
RUN python ez_setup.py
RUN curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
RUN python get-pip.py
RUN pip install virtualenv
