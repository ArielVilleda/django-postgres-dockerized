FROM python:3.8.3-alpine

# Initialize and Prepare
WORKDIR /data/web
# /web_app folder must contain the requirements.txt file
COPY /web_app /data/web/

RUN apk add --update build-base linux-headers gettext
RUN apk add --update postgresql-client postgresql-dev

# For images format and control
RUN apk add --update libmemcached-dev libjpeg tiff jpeg-dev zlib-dev freetype
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# Exposing the django wsgi port
EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
