from django.db import models


# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    # 定义varchar字段
    img_name = models.CharField(max_length=32)
    img_path = models.CharField(max_length=32)
    data = models.ImageField(upload_to='static/notedata')

    def __str__(self):
        return self.img_name
