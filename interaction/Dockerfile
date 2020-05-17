FROM ubuntu:18.04

ENV TERM linux

RUN apt-get -qq update && apt-get install -qq --no-install-recommends xinetd rsyslog python3 python3-pip vim
RUN apt-get install -qq python3-setuptools python3-dev git libssl-dev libffi-dev build-essential
RUN python3 -m pip install --upgrade pip

RUN pip install --upgrade pwntools

# For example:
#COPY requirements.txt /requirements.txt
#RUN pip3 install -r requirements.txt



COPY exploit1.sh /

COPY check1.py /
COPY check2.py /

RUN chmod +x /*.sh; chmod +x /*.py





