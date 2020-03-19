from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User,verbose_name="Пользователь",on_delete =models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.status} | {self.text} ==>{self.user.username}'