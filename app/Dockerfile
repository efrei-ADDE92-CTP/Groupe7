FROM python:3.8.3

ADD requirements.txt /tmp/requirements.txt

COPY knn.joblib ./

RUN pip install --upgrade pip

RUN pip install -r /tmp/requirements.txt

ADD app.py /var/server/app.py

CMD python /var/server/app.py
