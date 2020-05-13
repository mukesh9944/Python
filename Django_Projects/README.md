# Python Django Projects

## Installation
    
- create and activate the environment
> conda activate <myDjangoEnv>
- Python
> conda install python
- Django
> conda install django
- Bcyrpt
> conda install bcrypt
> conda install django[argon2]
- Pillow
> conda install pillow
            
        

## Basic commands

- Create a project
> django-admin createproject <projectName>

- Create a app under project (>cd projectName)
> django-admin createapp <appName>

- Migrate the app
> python manage.py migrate
> python manage.py makemigrations <appName>
> python manage.py migrate

- Start a server
> python manage.py runserver

- Create a superuser to login to admin
> python manage.py createsuperuser

    


