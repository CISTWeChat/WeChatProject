from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from Management.models import User
from Approval.models import TemplateId

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
    id_list = TemplateId.objects.all()      # 获取所有模板数据

    content = str('<div class=\"container\" style=\"margin-top: 10px; margin-left: 10px;\">\n'
            + '\t<table class=\"table table-striped\" style=\"width: 200px;\">\n'
            + '\t\t<thead style=\"font-weight:bold; line-height: 50px;\">\n'
            + '\t\t\t<td>Name</td>\n'
            + '\t\t\t<td>Action</td>\n'
            + '\t\t</thead>\n'
            + '\t\t<tr style=\"line-height: 20px;\">\n')

    for t_id in id_list:
        name = '\t\t\t<td>' + t_id.name + '</td>\n'
        action = '\t\t\t<td><a href=\"/Approval/show/'+ t_id.ID +'\">show</a></td>\n'
        content += name
        content += action
    
    content += str('\t\t</tr>\n'
            + '\t</table>\n'
            + '</div>')
    return HttpResponse(content)

# 信息采集
def showInfo(request):
    content = str('<div class=\"container\" style=\"margin-top: 10px; margin-left: 10px;\">\n'
            + '\t<table class=\"table table-striped\" style=\"width: 200px;\">\n'
            + '\t\t<thead style=\"font-weight:bold; line-height: 50px;\">\n'
            + '\t\t\t<td>信息采集</td>\n'
            + '\t\t</thead>\n'
            + '\t\t<tr style=\"line-height: 20px;\">\n'
            + '\t\t</tr>\n'
            + '\t</table>\n'
            + '</div>')

    return HttpResponse(content)