from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class News(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news', null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    img = models.URLField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
