#!/bin/bash

if lsof -i:5432; then
    echo "Port 5432 is in use. Attempting to stop the PostgreSQL service..."
    sudo systemctl stop postgresql
fi


if lsof -ti:5433; then
    echo "Port 5433 is in use. Attempting to kill the process..."
    sudo kill $(lsof -ti:5433)
fi

sudo docker-compose down -v
sudo docker-compose up --build
