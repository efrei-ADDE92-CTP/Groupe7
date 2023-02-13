# FROM python:3.8

# RUN apt update
# RUN apt install python3 -y

# # set the working directory in the container
# WORKDIR C:/Users/nostr/OneDrive/Documents/GitHub/Groupe7/app

# COPY app.py ./

# COPY knn.joblib ./
# # copy the dependencies file to the working directory
# COPY requirements.txt .

# # install dependencies
# RUN pip install -r requirements.txt

# ENV FLASK_APP=app.py

# EXPOSE 5000

# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt

ADD requirements.txt /tmp/knn.joblib

RUN pip install -r /tmp/requirements.txt

ADD app.py /var/server/app.py

CMD python /var/server/app.py