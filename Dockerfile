# pull official base image
FROM python:3.10.3-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables

#Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# add and install requirements
COPY ./requirements.txt .
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

# add app
COPY . .

# run server
CMD python manage.py run -h 0.0.0.0