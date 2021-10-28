from django.db import models
from django.urls.base import reverse
from group.models import Group
from user.models import Author
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=48)
    text = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post:post', kwargs={'pk':self.pk})



class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=256, default='Unknown')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post:post', kwargs={'pk':self.post.pk})

    def __str__(self) -> str:
        return self.text

    class Meta:
        ordering = ['-create_date']
