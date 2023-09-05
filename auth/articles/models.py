from django.db import models
#from accounts.models import User
from django.conf import settings
#from django.contrib.auth import get_user_model
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # 방법 1
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 방법 2
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 방법 3
    #user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)