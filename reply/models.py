from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Reply(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(
        Post, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    upvote = models.ManyToManyField(
        User, related_name='votes', blank=True)
    downvote = models.ManyToManyField(
        User, related_name='downvotes', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
