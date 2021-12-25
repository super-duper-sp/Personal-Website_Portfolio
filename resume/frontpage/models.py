from django.db import models

# Create your models here.
from django.db import models


class MAINpageContent(models.Model):
    Heading1 = models.CharField(max_length=30)
    Heading2 = models.CharField(max_length=30,null=True)
    buttonHeading = models.CharField(max_length=30)
    intro_pic = models.ImageField(upload_to='images/', null=True)

