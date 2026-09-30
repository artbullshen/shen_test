from django.db import models
from django.contrib.auth.models import User, AbstractUser

# 创建模型。
class BlogPost(models.Model):
    """博客模型,包含3个字段。"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        """返回模型的标题。"""
        return self.title

class Comment(models.Model):
    """博客列表中相关博客的评论。"""
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'

    def __str__(self):
        """返回模型的字符串表示。"""
        return f"{self.text[:20]}..."

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField('登录帐号', max_length=50, unique=True)
    password = models.CharField('密码', max_length=100)
    name = models.CharField('姓名',max_length=10)
    sex = models.CharField('性别',max_length=1)
    gradeClass = models.CharField('年级班级', max_length=15)
    jiguan = models.CharField('籍贯', max_length=30, null=True)
    icon = models.ImageField(upload_to='study/icon', null=True)

class Test(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.name

