#!/bin/bash

docker-compose up -d --build
docker-compose exec infra_web_1 python manage.py makemigrations users
docker-compose exec infra_web_1 python manage.py makemigrations recipes
docker-compose exec infra_web_1 python manage.py migrate --no-input
docker-compose exec infra_web_1 python manage.py collectstatic --no-input