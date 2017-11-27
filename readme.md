Proyecto Koilos

Install postgres 9.6.6

Install python 3.6

Install virtualenv   
	$ pip install virtualenv   
	
Create virtualenv in folder venv in project root   
	$ virtualenv venv

Activate virtualenv linux   
	$ source venv/bin/activate

Activate virtualenv windows   
	.>venv\Scripts\activate

Install requirements   
	$ pip install -r requirements.txt


Create db koilos_db

Migrate   
    $ python manage.py makemigrations   
    $ python manage.py migrate

Create superuser   
    $ python manage.py createsuperuser

Run app   
    $ python manage.py runserver 0.0.0.0:8001
    