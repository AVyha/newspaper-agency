from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(
        Topic, related_name="newspaper", on_delete=models.SET_NULL, null=True
    )
    publishers = models.ManyToManyField("Redactor", related_name="newspapers")

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)
    workplace = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["-years_of_experience"]
