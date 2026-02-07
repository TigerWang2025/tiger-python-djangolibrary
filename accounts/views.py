from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User


class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置中文标签
        self.fields['username'].lable = '用户名'
        self.fields['password1'].lable = '密码'
        self.fields['password2'].lable = '确认密码'

        # 自定义帮助文本
        self.fields['username'].help_text = '必填。150个字符或更少。只能包含字母、数字和 @/./+/-/_。'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = '为了确保安全，请输入与上面相同的密码。'

        # 自定义错误规则
        self.fields['username'].error_message = {
            'required': '用户名不能为空',
            'invalid': '请输入有效用户名',
            'unique': '该用户名已经被占用'
        }
        self.fields['password1'].error_message = {
            'required': '密码不能为空'
        }
        self.fields['password2'].error_message = {
            'required': '确认密码不能为空'
        }

    def clean_username(self):
        """验证用户名唯一性"""
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('该用户名已经被占用')
        return username


# Create your views here.
def register(request):
    # 判断是否是post提交
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        # 验证表单
        if form.is_valid():
            user = form.save()  # 存储数据
            username = form.cleaned_data.get('username')
            login(request, user)  # 注册后自动登录
            messages.success(request, f'账户{username}创建成功！您现在已登录。')
            return redirect('book_list')
        else:
            # 表单验证失败，将错误信息传回模板
            # messages.error(request, form.errors)
            messages.error(request, '注册失败，请检查下面的错误信息。')
    else:
        # GET 请求时创建空表单
        form = CustomerUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# def login(request):
#     """用户登录视图"""
#     # 这里放置登录逻辑
#     # 如果用户已经登录，重定向到主页
#     # if request.user.is_authenticated:
#     #     return redirect('home')
#
#     if request.method == 'POST':
#         # 获取表单提交的数据
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         # 验证用户凭据
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             # 登录用户
#             login(request, user)
#             messages.success(request, f'欢迎回来，{user.username}！')
#
# def logout(request):
#     """用户登出视图"""
#     # 这里放置登出逻辑
#     pass