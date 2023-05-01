# Data Engineering Project
This repository contains the code to provision PostgreSQL database and ingest and transform data from a csv file into the database. The dataset to ingest and transform is attachec in the repository. Python is used to write the code to ingest, transform and load the data into PostgreSQL database. The entire application is containerized using Docker and can be deployed locally. 

## Folder structure
+ etl: this folder contains the code to ingest, transform and load the data into PostgreSQL database. The code is written in python. The necessary dependencies are listed in requirements.txt
  + data - raw: dataset to ingest, transform and load
+ Dockerfile: this file contains the instructions to build the docker image that will run the python code. 
+ docker-compose.yml: this file contains the instructions to run the docker image as a container. This uses the Dockerfile to build the image and also creates a PostgreSQL database container.
+ .env: this file contains the environment variables that are used in docker-compose.yml

## Prerequisites
### Mac OS
1. Install Docker Desktop for Mac from https://docs.docker.com/docker-for-mac/install/

## Steps to run the application
1. Clone/Fork this repository
2. cd into project_directory [dataEngineeringProject]
3. Run `docker-compose up` # this will build the docker image and start the container
4. Check if number of rows loaded to the table is displayed in logs
5. Copy USERNAME and DATBASE from .env file
6. Open a new terminal session (Terminal - 2)and Run  `docker exec -it dataengineeringproject-postgres-database-1 psql -U <USERNAME> -d <DATABASE> -c "select count(*) from customers"` to check if the data is loaded in the table. 
7. To exit the container, ctrl + c on Terminal 1. 
8. Stop the container by running `docker-compose down` on Terminal 1.