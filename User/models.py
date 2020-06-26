from django.db import models


# Create your models here.
class Users(models.Model):
    userid = models.IntegerField(max_length=16, primary_key=True, verbose_name='用户id')
    username = models.CharField(max_length=32, null=False, verbose_name='用户名')
    password = models.IntegerField(null=False, verbose_name='用户密码')

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户信息表'


class UserToken(models.Model):
    username = models.OneToOneField(max_length=32, to='Users', on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=60)

    class Meta:
        db_table = 'user_token'
        verbose_name = verbose_name_plural = '用户token表'
