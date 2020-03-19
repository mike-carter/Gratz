from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    date_posted = models.DateTimeField('date posted')
    text = models.TextField(null=True)

    def get_post_summary(self):
        summary = self.text[:141]
        if len(self.text) > 140:
            summary += '...'
        return summary

    def get_absolute_url(self):
        return reverse('forum:post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField('date posted')
    text = models.TextField(null=True)

