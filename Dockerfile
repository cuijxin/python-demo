FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN pip install flask && pip install pyyaml
ADD . /usr/src/app

EXPOSE 5000
CMD python read-env-app.py
