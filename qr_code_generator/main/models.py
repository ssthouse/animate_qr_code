from django.db import models


# Create your models here.


class Dreamreal(models.Model):
    website = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phonenumber = models.IntegerField()

    # 配置数据库表名
    class Meta:
        db_table = 'dreamreal'


class GifModel(models.Model):
    url = models.CharField(max_length=100)
    colorful = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='static/pictures')

    class Meta:
        db_table = 'gif'
