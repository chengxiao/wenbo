# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

class AddForm(forms.Form):
    name = forms.CharField(label=u'姓名')
    age = forms.IntegerField(label=u'年龄')
    captcha = CaptchaField(label=u'验证码')
