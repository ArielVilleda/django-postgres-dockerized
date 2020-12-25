# Django, Postgres, Docker app

### Requisitos:
- Se utiliza la imagen base de docker `python:3.8.3-slim-buster`
- En el archivo `docker-compose`, se utiliza la imagen base de docker `postgres:12.4`

### Docker
- Para hacer build (o rebuild) de la imagen, desde la carpeta raíz del proyecto ejecutar `docker build -t django-app -f .\docker\Dockerfile . ` (-t para asignar un tag a la imagen, el cual nos es muy útil para los comandos a continuación)
- El comando `docker run --env-file ./path-to-web-app/.env -p 80:8000 django-app:latest` crea y pone en ejecución el container de la imagen especificada en el tag (en este ejemplo se tageó a la imagen con el nombre de `django-app` que automaticamente se le tageó la versión `latest`)
- Una vez en ejecución nuestro container (podemos comprobarlo con el comando `docker ps -a` el cual nos muestra el estatus de nestros containers) revisamos su id o su nombre, con el cual podemos acceder a ciertas operaciones de él, como puede ser acceder a su bash, etc
- Ejemplo: si el id del container en ejecución fuera 41985f87f328, podriamos acceder al bash (ya que el container se construyó a base de una imagen mínima de Linux, llamada alpine(Vease en el Dockerfile) y esta nos ofrece ciertas herramientas como comunicación con sh) de este con el comando `docker exec -i -t <name o id del container> /bin/sh`