from django.db import models

class BoardModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(null=True, blank=True)
    auther = models.CharField(null=True,max_length = 100)
    images = models.ImageField(upload_to='', blank=True)
    checked = models.BooleanField(null=True, blank=True, default=False)
    files = models.FileField(upload_to='', null=True, blank=True)
    branch = models.IntegerField(default=0)
    
