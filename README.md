# contact-app
A django App for saving data into models through CSV files, built with Django, Docker, pandas and postgresQL.


TO run the app, you first need to install Docker and Docker compose into your system

Using UBUNTU as a case study (you can research on how to do it for your own local system)
```
sudo apt-get update
sudo apt install docker.io
```

Then you will need to install *Docker-Compose* to be able to Build and run the docker Images.

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

Then you clone this repo

```
git clone https://github.com/Taycode/csvReader.git
cd contact-app
```

Now it is time to build the docker images and run 

```
docker-compose build
docker-compose up
```

Now the App would be running and you can access through 

http://localhost:8000/

# Architecture of the App

The app was built using Django, pandas and PostgresQL

The postgres database is on another container in which the django app container depends on

First you upload a csv file and input the name of the of the model you want to save it to

then you hit the submit button.

We use Pandas to read the file and write to the the db (read about Pandas, there is a to_sql and read_csv method that helps with that)

we also save the table name to a table called Table so we can identify the list of tables you have saved

It is from this we pull the list of tables and allow you to view the data in each Table

Enjoy using the App..

cheers, Tay
