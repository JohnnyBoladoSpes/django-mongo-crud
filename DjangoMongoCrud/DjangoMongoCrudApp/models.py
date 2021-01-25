#from django.db import models
from djongo import models
# Create your models here.
class Posts(models.Model):
    id=models.ObjectIdField()
    post_title=models.CharField(max_length=250)
    post_description=models.TextField()
    comment=models.JSONField()
    tags=models.JSONField()
    user_details=models.JSONField()
