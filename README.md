# bus-api
API for a Bus Agency  using Django REST framework
Requirements
Python 3.8
Django 3.1.2
Django REST Framework
Django Rest Auth

Installation
pip install Django==3.1.2
pip install djangorestframework

Structure
We will use the following URLS structure for the Classes Driver, Route, Bus and Passenger - /drivers/api/ and /drivers/api/<id> for collections and elements, respectively. 
Change the name according to the Class e.g. /routes/api/ or buses/api/


Use
We can test the API using curl or httpie. Httpie is a user friendly http client that's written in Python. Let's install that.

You can install httpie using pip:

pip install httpie
First, we have to start up Django's development server.

python manage.py runserver
Only authenticated users can use the API services. 

Super users are: Owner1 Password: Owner12020
                 User2  Password: User22020
