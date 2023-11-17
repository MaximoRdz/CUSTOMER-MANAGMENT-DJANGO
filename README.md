# CRM App with DJANGO
**CRM** stands for "Customer Relationship Managment", it is a technology that help businesses to organize and access customer data.
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
