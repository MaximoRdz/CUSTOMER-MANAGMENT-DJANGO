# CRM App with DJANGO
**CRM** stands for "Customer Relationship Managment", it is a technology that help businesses to organize and access customer data.
### Web Application Brief Summary
#### Register
New user can easily register filling the following form

<img width="500" alt="user registration" src="https://github.com/MaximoRdz/CUSTOMER-MANAGMENT-DJANGO/blob/main/images/register.gif" loading="lazy">
#### Create
Add customer record to database

<img width="500" alt="adding user to database" src="https://github.com/MaximoRdz/CUSTOMER-MANAGMENT-DJANGO/blob/main/images/create.gif" loading="lazy">
#### Read
Display of customer records

<img width="500" alt="displaying customer database" src="https://github.com/MaximoRdz/CUSTOMER-MANAGMENT-DJANGO/blob/main/images/read.gif" loading="lazy">
#### Update
Update an existing customer record

<img width="500" alt="updating customer record" src="https://github.com/MaximoRdz/CUSTOMER-MANAGMENT-DJANGO/blob/main/images/update.gif" loading="lazy">
#### Delete
Delete a customer record

<img width="500" alt="deleting customer record" src="https://github.com/MaximoRdz/CUSTOMER-MANAGMENT-DJANGO/blob/main/images/delete.gif" loading="lazy">

## Project Initialization
```cmd
django-admin startproject <crm>
cd <crm>
python manage.py starapp <website>
```
## CRM Main Steps
### Working with MySQL
Changing the security settings in order to connect to mysql databases
* Default sqlite3
	```python
	DATABASES = {
	    "default": {
	    "ENGINE": "django.db.backends.sqlite3",
	    "NAME": BASE_DIR / "db.sqlite3",
	    }
	}
	```
+ MySQL
	```python
	DATABASES = {
	        "default": {
	        "ENGINE": "django.db.backends.mysql",
	        "NAME": "crm_db",
	        "USER": "root",
	        "PASSWORD": "*******",
	        "HOST": "localhost",
	        "PORT": "3306",
	    }
	}
	```
### Creating a Super-User
```cmd
python manage.py createsuperuser
```
### Technologies
+ Django
+ MySQl
	```cmd
	pip install python-mysql-connector mysqlclient
	```
