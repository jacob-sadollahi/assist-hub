FROM python:3.11.1-slim-bullseye
ARG TARGETPLATFORM
RUN echo "I'm building for $TARGETPLATFORM"
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --allow-releaseinfo-change && apt-get upgrade -y && apt-get install -qqy \
    git \
    curl \
    wget \
    bzip2 \
    graphviz \
    libssl-dev \
    openssh-server \
    libgdk-pixbuf2.0-0 \
    gettext \
    libjpeg-dev \
    libatlas-base-dev \
    build-essential  \
    libffi-dev \
    libpq-dev \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    libgl1-mesa-dev \
    libglib2.0-0 \
    python-dev

RUN mkdir /var/run/sshd \
  && echo 'root:screencast' | /usr/sbin/chpasswd \
  && sed -i '/PermitRootLogin/c\PermitRootLogin yes' /etc/ssh/sshd_config \
  && sed -i '/AllowTcpForwarding/c\AllowTcpForwarding yes' /etc/ssh/sshd_config \
  # SSH login fix. Otherwise user is kicked off after login
  && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /usr/sbin/sshd \
  && echo "export VISIBLE=now" >> /etc/profile \
  && ssh-keygen -A
ENV NOTVISIBLE "in users profile"

# Create some folders
RUN mkdir -p /app | \
    mkdir -p /media-files | \
    mkdir -p /static-files

COPY ./requirements.txt /app/requirements.txt
COPY ./.coveragerc /.coveragerc
COPY ./sitecustomize.py /sitecustomize.py
RUN pip install -r /app/requirements.txt

COPY . /app

COPY ./scripts/* /scripts/
RUN chmod +x /scripts/*

WORKDIR /app

EXPOSE 8000
EXPOSE 22
