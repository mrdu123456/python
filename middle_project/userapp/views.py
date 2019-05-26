from datetime import datetime
from django.shortcuts import render,HttpResponse,redirect,reverse
from middle_project import settings
from modelapp.models import User,Code
from  captcha.image import ImageCaptcha
import os,random,uuid,string
import hashlib,random
from django.core.mail import EmailMultiAlternatives
# Create your views here.
# 发送邮箱验证码




def make_confirm_string():
    """
    为用户生成随机验证码并将验证码保存在数据库中
    :param new_user:
    :return:
    """
    code = random.sample(string.digits,5)
    code=''.join(code)
    return code


def send_email(email,code):
    subject, from_email, to = 'python157', '18000343457m@sina.cn', email
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册邮箱验证码为：{}，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '.format( code)
    #发送邮件所执行的方法以及所需的参数
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    # 发送的heml文本的内容
    msg.attach_alternative(html_content, "text/html")
    msg.send()



def getemail(request):
    """
    处理用户注册请求的view
    :param request: 用户的表单参数
    :return:
    """
    username = request.GET.get('txt_username')
    code=make_confirm_string()
    request.session['email']=code
    send_email( username,code)
    res=Code.objects.all()
    if res:
        res.delete()
    Code.objects.create(code=code)
    return HttpResponse('')

def delemail(request):
    del request.session['email']
    Code.objects.all().delete()
    print('删除成功')
    return HttpResponse('0')
# 加密
def getsalt():
    salt= random.sample(string.ascii_letters + string.digits, 3)
    s=''.join(salt)
    return s
def hash(pwd,salt):
    h=hashlib.md5()
    h.update((pwd + salt).encode())
    return h.hexdigest()

# 注册
def register(request):
    flag=request.GET.get('flag')
    request.session['flag']=flag
    targ = request.GET.get('targ')
    request.session['targ'] = targ
    return render(request,'userapp/register.html')

def registerlogic(request):
    res = Code.objects.all()
    sub=request.session.get('sub')
    txt_username=request.POST.get('txt_username')
    txt_password=request.POST.get('txt_password')
    if sub and  res:
        salt=getsalt()
        pwd=hash(txt_password,salt)
        request.session['uname']=txt_username
        user=User.objects.create(username=txt_username,password=pwd,email=txt_username,statue='0',salt=salt)
        url = reverse('userapp:registerok')+'?uname='+txt_username
        return redirect(url)
    else:
        return redirect('userapp:register')
def registerok(request):
    flag=request.session.get('flag')
    targ = request.session.get('targ')
    print(type(flag))
    if not flag:
        flag='1'
    uname=request.GET.get('uname')
    return render(request,'userapp/register ok.html',{'uname':uname,'flag':flag})


def ajax1(request):
    username=request.GET.get('username')
    flag=request.GET.get('flag')
    res=User.objects.filter(username=username)
    if flag=='2':
        return HttpResponse('999')
    else:
        if res:
            return HttpResponse('1')
        else:
            return HttpResponse('2')

def ajax2(request):
    code=request.GET.get('code')
    code1=request.session.get('code')
    if code.upper()==code1.upper():
        return HttpResponse('1')
    else:
        return HttpResponse('2')




def ajax3(request):
    uname=request.POST.get('uname')
    upwd=request.POST.get('upwd')
    upwd1=request.POST.get('upwd1')
    cap=request.POST.get('cap')
    code = request.session.get('code')
    user=User.objects.filter(username=uname)
    txt_mobile=request.POST.get('txt_mobile')
    emali=request.session.get('email')
    if not uname or not upwd or not code or not  txt_mobile:
        return  HttpResponse('4')
    elif user:
        return HttpResponse('1')
    elif upwd != upwd1:
        return HttpResponse('2')
    elif cap.lower() != code.lower():
        return HttpResponse('3')
    elif txt_mobile != emali:
        return HttpResponse('5')
    else:
        if not user and upwd == upwd1 and cap.lower()==code.lower() :
            request.session['sub']='ok'
            return HttpResponse('0')



# 登录
def login(request):
    flag = request.GET.get('flag')
    request.session['flag'] = flag
    targ=request.GET.get('targ')
    request.session['targ'] = targ
    if not flag:
        flag='1'
    return render(request,'userapp/login.html',{'flag':flag})

def loginlogic(request):
    flag=request.session.get('flag')
    targ=request.session.get('targ')
    txtUsername=request.POST.get('txtUsername')
    txtPassword=request.POST.get('txtPassword')
    che=request.POST.get('che')

    res=User.objects.filter(username=txtUsername)
    salt = res[0].salt
    pwd = hash(txtPassword, salt)
    if res[0].password==pwd:
        request.session['uname'] = txtUsername
        if flag=='home':
            result = redirect('booksapp:index')
        elif targ=='pay':
            result=redirect('orderapp:indent')
        if che:
            result.set_cookie('name', txtUsername, max_age=70000)
            result.set_cookie('password', txtPassword, max_age=70000)
        return result

def ajax4(request):
        cap = request.POST.get('cap')
        code = request.session.get('code')
        lname = request.POST.get('lname')
        print(cap)
        lpwd = request.POST.get('lpwd')
        print(lpwd)
        user = User.objects.filter(username=lname)
        salt =user[0].salt
        pwd = hash( lpwd, salt)
        if user[0].password==pwd and cap.lower() == code.lower():
            return HttpResponse('0')
        else:
            return HttpResponse('1')



# 验证码
def getcode(request):
    img=ImageCaptcha()
    code=random.sample(string.ascii_letters+string.digits,2)
    code=''.join(code)
    request.session['code']=code
    data=img.generate(code)
    return HttpResponse(data,'image/png')









