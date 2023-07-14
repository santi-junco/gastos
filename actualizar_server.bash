#!/bin/bash

cd /gastos

echo "Repository pull"
sudo git pull origin development

echo "Down container"
sudo docker-compose down

echo "Build container"
sudo docker-compose build

echo "Up container"
sudo docker-compose up -d

echo "Run migrations"
sudo docker-compose exec backend python manage.py migrate

echo "------- FIN -------"
