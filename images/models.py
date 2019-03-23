from django.db import models
from django.contrib.auth.models import User

from meetup.models import Meeting

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=50, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)
    meetup_id = models.ForeignKey(
        Meeting, on_delete=models.CASCADE)

    # def __str__(self):
    #     return (self.title, self.url)