from django.db import models
from django.utils import timezone
'''
Post 是模型的一个名字，我们可以给它取另外一个不同的名字
models.Model 表明Post是一个Django模型，所以Django知道它应该被保存在数据库中。

models.CharField - 这是你如何用为数有限的字符来定义一个文本。
models.TextField - 这是没有长度限制的长文本。
models.DateTimeField - 这是日期和时间.
models.ForeignKey - 这是指向另外一个模型的连接.
'''
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #文章标题的文本
    def __str__(self):
        return self.title