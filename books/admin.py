from django.contrib import admin
from .models import Book, BorrowRecord


# Register your models here.
# admin.site.register(Book) # 在管理台中归还图书，需要重新定义，用以下方法

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_available')
    search_fields = ('title', 'author')
    # search_fields = ('title', ) # 如果使用一个条件筛选，后边需要加 “,”   说明支持元组

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('user__username', 'book__title')  # 使用“__”，是因为user、book是关联的外键