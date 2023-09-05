from django.db import models
from django.conf import settings
from django_resized import ResizedImageField

# Create your models here.

class Question(models.Model):
    content = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option1_per = models.IntegerField(default=50)
    option2_per = models.IntegerField(default=50)
    option1_image = ResizedImageField(
        size = [500, 500],
        crop = ['middle', 'center'],
        upload_to='option1',
    )
    option2_image = ResizedImageField(
        size = [500, 500],
        crop = ['middle', 'center'],
        upload_to='option2',
    )
    # answer_set

class Answer(models.Model):
    option = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)