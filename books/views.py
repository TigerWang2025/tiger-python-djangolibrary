from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from books.models import Book, BorrowRecord


# Create your views here.
def book_list(request): # 图书列表页
    books = Book.objects.all()  #返回所有的图书列表信息
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)    # 根据book_id判断书是否存在，不存在返回404
    if book.is_available:
        BorrowRecord.objects.create(user=request.user, book=book)  # 保存借阅人信息
        book.is_available = False    # 将借阅状态改为不可借阅
        book.save()
        messages.success(request, f"成功借阅《 { book.title } 》")
    else:
        messages.error(request, f"《{ book.title } 》已被借阅")
    return redirect('book_list')

@login_required
def user_borrow_history(request):
    borrow_records = BorrowRecord.objects.filter(user=request.user).order_by('-borrow_date')  # 根据借阅时间进行降序排序，“-”表示降序
    return render(request, 'books/borrow_history.html', {'borrow_records': borrow_records})
