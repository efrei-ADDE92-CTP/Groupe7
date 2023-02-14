FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt

ADD requirements.txt /tmp/knn.joblib

RUN pip install -r /tmp/requirements.txt

ADD app.py /var/server/app.py

CMD python /var/server/app.py