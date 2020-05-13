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

## Deployment

- https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
- https://devcenter.heroku.com/articles/deploying-python
- https://www.digitalocean.com/community/tutorials/how-to-deploy-a-local-django-app-to-a-vps



