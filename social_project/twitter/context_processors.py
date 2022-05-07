# from django.contrib.auth.models import User
from .models import Profile
from django.db.models import *


def users_links(request):
    users_link = Profile.objects.all().order_by('?')
    return dict(users_link=users_link)