FROM python:3.9.6-slim-buster

#set working dir
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  #Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1          #Prevents Python from buffering stdout and stderr

#install system dependancies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean \


# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# add app
COPY . .

## add entrypoint.sh
#COPY ./entrypoint.sh .
#RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]
#
##execute entrypoint for DB startup
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]