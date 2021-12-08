# _*_coding: utf-8_*_
#
# @Project_Name:cnblog
# @File_name: Myforms
# @author: kyle
# @date: 2021/12/5 17:08
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from blog.models import UserInfo


class UserForm(forms.Form):

    user = forms.CharField(max_length=32,
                           error_messages={"required": "该字段不能为空"},
                           label="用户名",
                           widget=widgets.TextInput(attrs={"class": "form-control"}, ))

    pwd = forms.CharField(max_length=32,
                          error_messages={"required": "该字段不能为空"},
                          label="密码",
                          widget=widgets.PasswordInput(attrs={"class": "form-control"}, ))

    re_pwd = forms.CharField(max_length=32,
                             error_messages={"required": "该字段不能为空"},
                             label="确认密码",
                             widget=widgets.PasswordInput(attrs={"class": "form-control"}, ))

    email = forms.EmailField(max_length=32,
                             error_messages={"required": "该字段不能为空"},
                             label="邮箱",
                             widget=widgets.EmailInput(attrs={"class": "form-control"}, ))
    # avatar = models.FileField(upload_to='avatars/', default="avatars/default.png")

    def clean_user(self):
        # 校验是否存在
        val = self.cleaned_data.get("user")
        # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
        user = UserInfo.objects.filter(username=val).first()

        if not user:
            return val
        else:
            raise ValidationError("该用户已注册！")

    def clean(self):

        # cleaned_data 就是读取表单返回的值，返回类型为字典dict型
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")

        if pwd and re_pwd:
            if pwd == re_pwd:
                return self.cleaned_data
            else:
                raise ValidationError("两次密码不一致！")
        else:
            return self.cleaned_data
