from django.db import models
from django.db.models.fields import CharField
from user.models import *
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=96, unique=True)
    slug = models.SlugField(max_length=96, default="add-slug-all-groups")
    describtion = models.CharField(max_length=96, default='Without Description')
    owner = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Groups', blank=True)
    created_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name


class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")
