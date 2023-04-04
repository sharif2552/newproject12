from django.db import models

# Create your models here.
class blog(models.Model):
    name=models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name