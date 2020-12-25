FROM python:3.8.3-slim-buster

# Initialize and Prepare
WORKDIR /data/web

# Copying the requirements.txt file first
COPY /web_app/requirements.txt /data/web/
# Install python requirements
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# In the last steps of Dockerfile, coopying the others files 
# to avoid reinstallation of dependecies if files changes
COPY /web_app /data/web/

# Exposing the django wsgi port
EXPOSE 8000 
