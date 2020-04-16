FROM python:3.7.7-slim-buster

COPY . /local
WORKDIR /local
RUN apt-get update && cat requirements.system | xargs apt-get install -y
RUN mkdir /opt/ntc-templates && \
    git clone https://github.com/networktocode/ntc-templates.git /opt/ntc-templates

RUN pip install --no-cache -r requirements.txt
RUN ansible-galaxy collection install -r requirements.yml
CMD /bin/bash