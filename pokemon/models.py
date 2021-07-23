from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Pokemon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    pokemon = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.pokemon

    class Meta:
        db_table = "pokemon"