from django.db import models

# Create your models here.
class UserType(models.Model):
    '''
    定义用户类型：普通用户、管理员
    '''
    title=models.CharField(max_length=32)

class UserInfo(models.Model):
    '''
    定义用户表:用户与用户类型之间是一对多的关系,通过外键ut来维护
    '''
    username=models.CharField("用户名",max_length=32)
    pwd=models.CharField("密码",max_length=32)
    email=models.CharField(max_length=15)
    ut=models.ForeignKey(to="UserType",to_field="id")


class BusinessInfo(models.Model):
    """
    定义业务表:业务与用户之间是多对多的关系:通过mm字段来进行维护
    """
    businessname = models.CharField('业务线名称',max_length=32)

    mm = models.ManyToManyField('UserInfo')

class HostInfo(models.Model):
    """
    定义主机表:主机与业务之间是一对多的关系,一个主机对应多个业务,通过busid字段来进行维护
    """
    hostname = models.CharField('主机名',max_length=32)
    port = models.CharField('端口',max_length=10)

    busid = models.ForeignKey(to='BusinessInfo',to_field='id')