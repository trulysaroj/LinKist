from django.db import models
from django.forms import URLField


# Create your models here.
class Profile(models.Model):
    BG_CHOICES = (
        ('black', 'Black'),
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=20, choices=BG_CHOICES)

    def __str__(self):
        return self.name


class Link(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return f"{self.title} | {self.url}"
