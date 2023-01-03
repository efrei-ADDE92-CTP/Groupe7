FROM python:3.8

RUN apt update
RUN apt install python3 -y

# set the working directory in the container
WORKDIR C:/Users/nostr/OneDrive/Documents/GitHub/Groupe7

COPY app.py ./

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
#CMD ["flask", "run", "--host", "0.0.0.0:8081"]
CMD [ "python3", "./app.py" ]