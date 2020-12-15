from django.db import models

# Create your models here.
class Watch(models.Model):
    name = models.CharField(max_length=100)
    prize = models.IntegerField()
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save_watch(self):
        self.save()

    def delete_watch(self):
        self.delete()