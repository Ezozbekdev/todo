from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Main(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    created_data = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="main/img/")

    def __str__(self):
        return self.title
