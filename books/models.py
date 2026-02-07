from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=108, verbose_name='书名')
    author = models.CharField(max_length=88, verbose_name='作者')
    cover = models.ImageField(upload_to='covers/', verbose_name='图书封面')
    is_available = models.BooleanField(default=True, verbose_name='是否可借')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '图书'
        verbose_name_plural = '图书'


class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='借阅人')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='图书')
    borrow_date = models.DateTimeField(auto_now_add=True, verbose_name='借阅时间')
    return_date = models.DateTimeField(null=True, blank=True, verbose_name='归还时间')

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"

    class Meta:
        verbose_name = '借阅管理'
        verbose_name_plural = '借阅管理'
