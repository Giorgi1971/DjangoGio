from .models import Profile


def users_links(request):
    users_link = Profile.objects.all().order_by('?')
    return dict(users_link=users_link)
