from django.db import models
from django.urls.base import reverse
from group.models import Group
from user.models import Author
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=96)
    description = models.CharField(max_length=144, default="Write another dexcription")
    text = models.TextField()
    group = models.ManyToManyField(Group)
    image = models.ImageField(upload_to='Posts', blank=True)

    create_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('post:post', kwargs={'pk':self.pk})



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, default='Unknown')
    text = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post:post', kwargs={'pk':self.post.pk})

    def __str__(self) -> str:
        return self.text

    class Meta:
        ordering = ['-create_date']
