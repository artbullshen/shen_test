

class MyUser(AbstractUser):
    qq = models.CharField(u'qq号', max_length=16)
    weChat = models.CharField(u'微信帐号', max_length=100)
    mobile = models.CharField(u'手机号',primary_key=True, max_length=11)

    # 添加其它自定义字段

    def __str__(self):
        return self.username



