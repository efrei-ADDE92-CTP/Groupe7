FROM python:3.8

RUN apt update
RUN apt install python3 -y

# set the working directory in the container
WORKDIR /app

COPY app/app.py ./

COPY app/knn.joblib ./
# copy the dependencies file to the working directory
COPY app/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]