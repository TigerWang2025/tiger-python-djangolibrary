from django.urls import path
from books import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # URL中的首页显示，不需要指向某个目录
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('borrow/<int:book_id>', views.borrow_book, name='borrow_book'),
    path('borrow_history/', views.user_borrow_history, name='user_borrow_history'),
]