import hashlib
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import json
import index.static.manage.DepartmentalManagement
# Create your views here.

def Index_Views(request):
    ucompany = index.static.manage.DepartmentalManagement.ucompany
    udepartment1 = index.static.manage.DepartmentalManagement.udepartment1
    udepartment2 = index.static.manage.DepartmentalManagement.udepartment2
    if request.method == 'GET':
        # 判断cookie
        mysession = request.session.get('uname')
        if mysession:
            # 用户已登录直接跳转管理界面
            return Management_Views(request)
        else:
            # 用户未登录访问登录界面
            return render(request, 'index.html')
    else:
        # 获取登录账号与密码
        uphone = request.POST.get('uphone', '')
        upass = request.POST.get('upassword', '')
        # 判断账号密码是否为空
        if uphone and upass:
            # 获取数据库信息
            users = login.objects.filter(u_phone=uphone)
            # 判断用户是否存在
            if users:
                # 获取数据库用户信息
                u = users[0]
                # 创建MD5
                md = hashlib.md5()
                # 一次转码
                md.update(upass.encode('utf8'))
                upass = md.hexdigest()
                # 二次转码
                md.update(upass.encode('utf8'))
                upass = md.hexdigest()
                # 判断密码是否正确
                if upass == u.u_pass:
                    # 设置页面跳转传递参数
                    resp = Management_Views(request)
                    # 设置COOKIE的参数
                    resp.set_cookie('uphone', u.u_phone, 60*60*2)
                    resp.set_cookie('id', u.id, 60*60*2)
                    # 设置SESSION的参数
                    request.session['login_id'] = u.id
                    request.session['level'] = u.level
                    request.session['uname'] = u.u_name
                    request.session['ucompany'] = ucompany[u.u_company]
                    request.session['udepartment1'] = udepartment1[u.u_department1]
                    try:
                        request.session['udepartment2'] = udepartment2[u.u_department1][(int(u.u_department2)-1)]
                    except (TypeError, KeyError, IndexError):
                        request.session['udepartment2'] = '空'
                    request.session['upost'] = u.u_post
                    request.session.set_expiry(0)
                    # 页面跳转
                    return resp
                # 错误返回登录界面
                else:
                    errMsg = '密码错误'
                    return render(request, 'index.html', locals())
            else:
                errMsg = '用户不存在'
                return render(request, 'index.html', locals())
        # 验证错误返回登录
        else:
            errMsg = '手机或密码不能为空'
            return render(request, 'index.html', locals())

def Register_Views(request):
    ucompany = index.static.manage.DepartmentalManagement.ucompany
    udepartment1 = index.static.manage.DepartmentalManagement.udepartment1
    udepartment2 = index.static.manage.DepartmentalManagement.udepartment2
    # 注册界面判定GET与POST
    if request.method == 'GET':
        # 去往注册界面
        return render(request, 'register.html', {'ucompany': json.dumps(ucompany),
                                                 "udepartment1":  json.dumps(udepartment1),
                                                 "udepartment2":  json.dumps(udepartment2)})

    # 接收登录界面提交信息
    else:
        uphone = request.POST.get('uphone', '')
        upassword = request.POST.get('upassword', '')
        uname = request.POST.get('uname', '')
        unameid = request.POST.get('unameid', '')
        ucompany = request.POST.get('ucompany', '')
        udepartment1 = request.POST.get('udepartment1', '')
        udepartment2 = request.POST.get('udepartment1', '')
        upost = request.POST.get('upost', '')
        # 判定提交数据是否位空
        if uphone and upassword and uname and unameid:
            # 依据手机号查询数据库
            u = login.objects.filter(u_phone=uphone)
            # 判定注册账号与数据库是否重复
            if u:
                # 注册长号重复提示
                errMsg = '手机号码已存在'
                return render(request, 'register.html', locals())
            # 创建新账号
            else:
                # 密码转MD5
                md = hashlib.md5()
                # 一次转码
                md.update(upassword.encode('utf8'))
                upassword = md.hexdigest()
                # 二次转码
                md.update(upassword.encode('utf8'))
                upassword = md.hexdigest()
                # 注册信息存入数据库
                login.objects.create(u_phone=uphone,
                                     u_pass=upassword,
                                     u_name=uname,
                                     u_ID=unameid,
                                     u_company=ucompany,
                                     u_department1=udepartment1,
                                     u_department2=udepartment2,
                                     u_post=upost)
                # 去往注册成功界面
                return render(request, 'jump.html')
        # 注册信息填写有误
        else:
            return HttpResponse('请验证您的输入')

# 个人管理界面
def Management_Views(request):
    return HttpResponseRedirect('/management/')
# 注销登录
def Quit_Views(request):
    del request.session['uname']
    return HttpResponseRedirect('/')
