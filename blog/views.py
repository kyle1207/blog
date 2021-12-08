# _*_coding: utf-8_*_
#
# @author: kyle
# @date: 2021/12/5 17:08

from django.contrib import auth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from blog import models
from blog.Myforms import UserForm
from blog.models import UserInfo
from blog.utils import validCode


def login(request):
    if request.method == "POST":
        response = {"user": None, "msg": None}

        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        valid_code = request.POST.get("valid_code")
        valid_code_str = request.session.get("valid_code_str")
        if valid_code.upper() == valid_code_str.upper():
            user = auth.authenticate(username=user, password=pwd)
            if user:
                auth.login(request, user)  # request.user == 当前登陆对象
                response["user"] = user.username
            else:
                # alert("username or password error!")
                response["msg"] = "user or password error!"
        else:
            response["msg"] = "valid code error!"
        return JsonResponse(response)
    return render(request, "login.html")


def get_validCode_img(request):
    """
    基于PIL模块动态生成响应状态码图片
    :param request:
    :return:
    """
    img_data = validCode.get_valid_code_img(request)
    return HttpResponse(img_data)


def index(request):
    article_list = models.Article.objects.all()
    return render(request, "index.html", {"article_list": article_list})


def register(request):
    # 提交检验
    if request.is_ajax():
        # print(request.POST)
        form = UserForm(request.POST)

        response = {"user": None, "msg": None}
        if form.is_valid():
            response["user"] = form.cleaned_data.get("user")

            # 生成一条用户记录
            user = form.cleaned_data.get("user")
            print("user:", user)
            pwd = form.cleaned_data.get("pwd")
            email = form.cleaned_data.get("email")

            avatar_obj = request.FILES.get("avatar")
            extra = {}
            if avatar_obj:
                extra["avatar"] = avatar_obj
                # user_obj = UserInfo.objects.create_user(username=user, password=pwd, email=email, avatar=avatar_obj)
                # user_obj = UserInfo.objects.create_user(username=user, password=pwd, email=email, **extra)
                UserInfo.objects.create_user(username=user, password=pwd, email=email, **extra)

        else:
            print(form.cleaned_data)
            print(form.errors)
            response["msg"] = form.errors
        return JsonResponse(response)

    form = UserForm()
    return render(request, "register.html", {"form": form})


def logout(request):
    # 等同于 request.session.flush()
    auth.logout(request)
    return redirect("/login/")
