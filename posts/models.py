from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    image_filter_choices = [
        ('NO_FILTER', 'no filter'),
        ('COLORIZED', 'colorized'),
        ('GRAYSCALE', 'grayscale'),
        ('BLURRED', 'blurred'),
        ('BINARY', 'binary'),
        ('INVERT', 'invert'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_hl6wjy.png', blank=True
    )
    image_filter = models.CharField(
        max_length=30, choices=image_filter_choices, default='normal'
    )
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    no_of_likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
