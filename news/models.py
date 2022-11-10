from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(
        max_length=255
    )


class Newspaper(models.Model):
    title = models.CharField(
        max_length=255
    )
    content = models.TextField(
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        auto_now_add=True
    )
    topic = models.ForeignKey(
        Topic,
        related_name="newspaper",
        on_delete=models.SET_NULL,
        null=True
    )
    publishers = models.ManyToManyField(
        "Redactor",
        related_name="newspapers"
    )


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()


