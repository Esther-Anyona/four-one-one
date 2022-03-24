# Four-one-one

## Description

A django web application that allows a user to keep up with what is happening in their neighbourhood. A user has to update the neighbourhood they live in after signing up. A user can view posts and business from their neighbourhood only. A user cannot belong to more than one neighbourhood.

## Author

[Esther-Anyona](https://github.com/Esther-Anyona)

## BDD
- User signs up.
- User views existing neighbourhoods.
- User updates their profile to indicate their neighbourhood.
- User views posts and businesses from their neighbourhood.
- User can add a new post or business
- User can update their neighbourhood if they move.

## Deployment

Install heroku CLI to deploy on heroku
* Add a Procfile in the project root;
* Add requirements.txt file with all the requirements in the project root;
* Add Gunicorn to requirements.txt;
* A runtime.txt to specify the correct Python version in the project root;
* Configure whitenoise to serve static files.


## Tools and Technologies

* Python3.8
* Django==4.0.2
* Bootstrap v5
* postgresql
* Heroku


## Setting up the project locally

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
1. git clone the repository
    - https://github.com/esther-anyona/four-one-one.git
1. cd into app directory
    - cd four_one_one
1. create a virtual env
    -  python3 -m venv virtual
1. activate virtual environ
    - source virtual/bin/activate
1. Install all dependancies
1. Make Migrations
python3 manage.py makemigrations
    - Apply migrations to database
    - python3 manage.py migrate
1. To run the app on localhost
    - python3 manage.py runserver


## Creating .env

Required file to keep sensitive data that should not be exposed in github

SECRET_KEY = '<Secret_key>'

DBNAME = 'awards'

USER = '<Username>'

PASSWORD = '<password>'

DEBUG = True

EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_HOST_USER = '<your-email>'

EMAIL_HOST_PASSWORD = '<your-password>'

cloudinary_api_key=<cloudinary api_key>
cloudinary_secret=<cloudinary api_secret>
cloud_name=<cloudinary cloud_name>

## Running the tests

To run tests for this application in development:
1. run python3 manage.py test

### Prerequisites

The application requires the following installations to operate:

* pip
* gunicorn
* django
* psycopg2
* cloudinary

## Contact

You can reach me through:
* Email: jkemuntoe@gmail.com or
* Phone: +254724374477

## License

*MIT License*:
Copyright (c) 2022 *Esther Anyona*