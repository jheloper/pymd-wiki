FROM ubuntu:xenial
LABEL maintainer="jheloper9102@gmail.com"
ENV REFRESHED_AT=2017-12-31

RUN sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list && \
    apt update && \
    apt install -y --no-install-recommends build-essential python python3 software-properties-common && \
    add-apt-repository -y ppa:jonathonf/python-3.6 && \
    apt update && \
    apt install -y --no-install-recommends python3.6 python3.6-venv && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 80