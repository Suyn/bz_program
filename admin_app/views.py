import random
import string
import os
import re
import uuid

from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from admin_app.utils import checkMail,checkMobile
# Create your views here.
#生成一个验证码 并将图片，写出给浏览器
from admin_app.models import User
# from demo_sms_send import send_sms
from dysms_python.demo_sms_send import send_sms
from dysms_python import demo_sms_send as send
from lib.captcha.image import ImageCaptcha



def getcaptcha(request):
    # print('##############333')
    # 从image.py中导入ImageCaptcha类，ImageCaptcha是图片验证码的核心类
    # 为验证码设置字体，获取项目目录下的字体文件
    imgage = ImageCaptcha(fonts=[os.path.abspath('lib/captcha/verdana.ttf')])
    # 随机码
    # 大小写英文字母+数字，并随机取5位作为验证码
    code = "".join(random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,4))
    print('验证码：', code)
    # code是一个列表 用join转换成字符串
    # 将验证码存入session，以备后续验证
    request.session["code"] = code
    # 将生成的随机字符拼接成字符串，作为验证码图片中的文本
    data = imgage.generate("".join(code))
    # 写出验证图片给客户端 告知浏览器，写出的内容是一图片
    return HttpResponse(data,"image/png")


# ajax异步验证验证码
def check_captcha(request):
    number=request.POST.get("number")
    num=request.session.get("code")
    if num.lower()==number.lower():
        return HttpResponse("ok")
    return HttpResponse("error")

#注册时ajax异步验证phone
def check_phone(request):
    phone=request.POST.get("usrtel")
    print('###########',phone)
    if not phone:
        return HttpResponse("0")
    user = User.objects.filter(phone=phone)
    print('!!!!!!!!!!!',user)
    if not user:
        return HttpResponse('1')
    return HttpResponse("2")

#ajax异步验证昵称
def check_nike(request):
    phone=request.POST.get("username")
    if not phone:
        return HttpResponse("0")
        user = User.objects.filter(phone=phone)
        if not user:
            return HttpResponse('2')
    return HttpResponse("1")

#ajax异步验证password
def check_pwd(request):
    phone = request.POST.get("username")
    password = request.POST.get("password")
    user = User.objects.filter(phone=phone)
    if not user:
        return HttpResponse('0')
    if user:
        check = check_password(password, User.objects.get(phone=phone).password)
        if check:
            return HttpResponse('1')
    return HttpResponse('2')


def regist_page(request):
    return render(request,"admin_app/register.html")

def regist_logic(request):
    userid=request.POST.get('userid')
    usrtel=request.POST.get('usrtel')
    email=request.POST.get('email')
    psw=request.POST.get('psw')
    password=make_password(psw) #传入密文
    user=User(email=email, username=userid, password=password, phone=usrtel)
    user.save()
    request.session["name"]=usrtel
    return redirect('back_end:show_index')

def login_page(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
    else:
        ip = request.META.get('REMOTE_ADDR')
    request.session['ip']=ip
    return render(request,"admin_app/index.html")

def login_logic(request):
    #接受参数
    phone=request.POST.get("username")
    password=request.POST.get("password")
    user=User.objects.filter(phone=phone)
    if user:
        check=check_password(password,User.objects.get(phone=phone).password)
        if check:
            #phone存session
            request.session["name"] = User.objects.get(phone=phone).phone
            #重定向到展示view
            return redirect('back_end:show_index')
            # return redirect("order:settle_accounts")
        else:
            err = '密码错误，请重新登录!'
            return render(request, "admin_app/index.html",{'err':err})
    err1 = '用户名错误，请重新登录!'
    return render(request,"admin_app/index.html",{'err1':err1})

def send_code(request):
    phone = request.POST.get("phone")
    print(phone)
    code="".join(random.sample(string.digits,6))
    request.session['real_code']=code
    print(code)
    __business_id = uuid.uuid1()
    params = u'{"code":' + code + '}'
    print(send.send_sms(__business_id,phone, "广告", "SMS_29435071", params).decode('utf-8'))
    return HttpResponse('ok')

def login_logic_phone(request):
    #接受参数
    real_code=request.session.get('real_code')
    phone=request.POST.get("username")
    code=request.POST.get("code")
    user=User.objects.filter(phone=phone)
    print(real_code,phone,code)
    if user:
        if real_code==code:
            #phone存session
            request.session["name"] = User.objects.get(phone=phone).phone
            #重定向到展示view
            print('--------------->  Success')
            return redirect('back_end:show_index')
            # return redirect("order:settle_accounts")
        else:
            errphone = '验证码错误，请重新登录!'
            return render(request, "admin_app/index.html",{'errphone':errphone})
    errphone1 = '用户名错误，请重新登录!'
    return render(request,"admin_app/index.html",{'errphone1':errphone1})