from django.urls import path
from books import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # URL中的首页显示，不需要指向某个目录
    path('books/<int:book_id>', views.book_detail, name='book_detail'),
    path('borrow/<int:book_id>', views.borrow_book, name='borrow_book'),
    path('borrow_history/', views.user_borrow_history, name='user_borrow_history'),

    # 修改密码 (用户已登录状态下)
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html'
    ), name='password_change'),

    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'
    ), name='password_change_done'),
]