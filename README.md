# DjangoGio

## This is a Twitter clone, ABOUT social_project!
### This project corresponds to the youtube tutorial:
#### To use/configure it:
* Clone the repository or download it as a zip.
* git clone https://github.com/mundo-python/social_project.git
* Create a virtual environment
* python -m venv socialenv
* Install dependencies/libraries in requirements.txt
* pip in* stall -r requirements.txt
* Run th* e migrations.
* python*  manage.py makemigrations python manage.py migrate
* Create*  a super user.
* python*  manage.py createsuperuser
* Run the server.
* python manage.py runserver
## news:
* django.contrib.humanize (for "25 minutes ago")
*                         {% if request.user.is_authenticated %}
                            {% if user.username != request.user.username %}
                                {% if user not in request.user.profile.following %}
