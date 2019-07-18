from django.db import models

from django.db import models

# Create your models here.
class Huaban(models.Model):
    name = models.TextField(max_length=30)
    imgurl = models.TextField(max_length=100)
    imgherf = models.TextField(max_length=100)
    imgvisit = models.TextField(max_length=20)
    imglike = models.TextField(max_length=20)
    imgdiscrit = models.TextField(max_length=50,null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'huaban'
