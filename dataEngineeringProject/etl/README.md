# ETL using Python
Ingest, transform and load data from a csv file into PostgreSQL database. The dataset to ingest and transform is attachec in the repository. Python is used to write the code to ingest, transform and load the data into PostgreSQL database. The entire application is containerized using Docker and can be deployed locally.

## Folder structure
+ data - raw: dataset to ingest, transform and load
+ etl.py: main python executable file called by Dockerfile. This file orchestates the code to ingest, transform and load the data into PostgreSQL database.
+ extract.py: this file contains the code to ingest the data from csv file
+ transform.py: this file contains the code to transform the data
+ load.py: this file contains the code to load the data into PostgreSQL database
+ config.py: this file contains the configuration to connect to PostgreSQL database

## Prerequisites (to test python scripts locally)
### Mac OS
Python 3.10.2

## Steps to test python scripts locally
1. Clone/Fork the repository
2. cd into project_directory [dataEngineeringProjects/etl]
3. Run `pip install -r requirements.txt` to install the dependencies
4. Run `python extract.py` to ingest the data from csv file
5. Run `python transform.py` to transform the data