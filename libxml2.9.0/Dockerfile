FROM ubuntu:precise

RUN echo "deb http://ja.archive.ubuntu.com/ubuntu/ precise universe" >> /etc/apt/sources.list
RUN echo "deb http://ja.archive.ubuntu.com/ubuntu/ precise-updates universe" >> /etc/apt/sources.list

RUN apt-get update -y
RUN apt-get install -y build-essential
RUN apt-get install -y curl
RUN apt-get install -y wget
RUN apt-get install -y git
RUN apt-get install -y python
RUN apt-get install -y python-dev
RUN apt-get install -y python-virtualenv
RUN apt-get install -y automake autoconf libtool
RUN apt-get install -y libz-dev

RUN cd /root/ && wget https://git.gnome.org/browse/libxml2/snapshot/libxml2-2.9.0.tar.gz
RUN cd /root/ && tar zxvf libxml2-2.9.0.tar.gz
RUN cd /root/libxml2-2.9.0 && ./autogen.sh
RUN cd /root/libxml2-2.9.0 && make
RUN cd /root/libxml2-2.9.0 && make install

RUN cd /root/ && wget https://git.gnome.org/browse/libxslt/snapshot/libxslt-1.1.28.tar.gz
RUN cd /root/ && tar zxvf libxslt-1.1.28.tar.gz
RUN cd /root/libxslt-1.1.28 && ./autogen.sh
RUN cd /root/libxslt-1.1.28 && make
RUN cd /root/libxslt-1.1.28 && make install

RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/usr-local-lib.conf
RUN ldconfig -v

RUN pip install lxml==3.1.2
