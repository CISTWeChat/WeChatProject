from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from Management.models import User

# 验证登录
def login(request):
    return render(request,"Management/login.html")

def loginRes(request):
    uid = request.POST.get('uid')
    pwd = request.POST.get('pwd')

    try:
        user = User.objects.get(id=uid)
    except User.DoesNotExist:
        user = None
    
    if(user):
        if(pwd == user.password):
            request.session['uid'] = uid
            request.session['isLogin'] = True
            return render(request,'Management/index.html',{'uid':uid})
        else:
            return render(request,'Management/login.html',{'login_msg':'用户名或密码错误!'})
    else:
        return render(request,'Management/login.html',{'login_msg':'用户不存在!'})

def logout(request):
    request.session['isLogin'] = None
    return render(request,'Management/login.html',{'login_msg':''})

# 访问主页
def index(request):
    if request.session.get('isLogin'): 
        return render(request,'Management/index.html',{'uid':request.session.get('uid')})
    else:
        return render(request,'Management/login.html',{'login_msg':''})

# 审批
def showApproval(request):
    return render(request,'Management/showApproval.html')
    

# 信息采集
def showInfo(request):
    return render(request,'Management/showInfo.html')