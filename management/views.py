import random
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from index.models import login
from .models import *
from management.static.manage.question_type import *



# Create your views here.



# 选择题数据库提取
def SelectSubject(mylist,long,s):
    l = [[[], []], []]
    ls = random.sample(range(0, long), s)
    for x in ls:
        subject = mylist[x].subject
        a_option = mylist[x].a_option
        b_option = mylist[x].b_option
        c_option = mylist[x].c_option
        d_option = mylist[x].d_option
        answer = mylist[x].answer
        l[0][0].append(subject)
        l[0][1].append([a_option, b_option, c_option, d_option])
        l[1].append(answer)
    return l

def JudgeShortanswerSubject(mylist, long, s):
    l = [[], []]
    ls = random.sample(range(0, long), s)
    for x in ls:
        subject = mylist[x].subject
        answer = mylist[x].answer
        l[0].append(subject)
        l[1].append(answer)
    return l


# 获取试题函数
def Ks(request, table, ks, n1, n2, n3, n4, n5):
    try:
        uname = request.session.get('uname', '')
        # 获取题库
        select_one = table.objects.filter(question_type='1')
        long1 = len(select_one)
        # 生成10道选择题
        select_one = SelectSubject(select_one, long1, n1)

        select_more = table.objects.filter(question_type='2')
        long2 = len(select_more)
        # 生成10道多选题
        select_more = SelectSubject(select_more, long2, n2)

        judge = table.objects.filter(question_type='3')
        long3 = len(judge)
        # 生成10道判断题
        judge = JudgeShortanswerSubject(judge, long3, n3)

        completion = table.objects.filter(question_type='4')
        long4 = len(completion)
        # 生成5道简答题
        completion = JudgeShortanswerSubject(completion, long4, n4)

        short_answer = table.objects.filter(question_type='5')
        long5 = len(short_answer)
        # 生成5道简答题
        short_answer = JudgeShortanswerSubject(short_answer, long5, n5)

        subject1 = select_one[0][0]+select_more[0][0]+judge[0]+completion[0]+short_answer[0]
        subject2 = select_one[0][1]+select_more[0][1]
        subject = [subject1, subject2]
        answer = select_one[1]+select_more[1]+judge[1]+completion[1]+short_answer[1]
    except Exception:
        return HttpResponse('请检查题库题目数量是否满足最低需求')
    if uname:
        return render(request, ks, {
            "subject": json.dumps(subject),
            "answer": json.dumps(answer),
            'uname': uname,
            'ucompany': request.session.get('ucompany', ''),
            'udepartment1': request.session.get('udepartment1', ''),
            'udepartment2': request.session.get('udepartment2', ''),
            'upost': request.session.get('upost', ''),
        })
    else:
        return HttpResponseRedirect('/')

# 去入职安全考试界面
def Rzaqks_Views(request):
    return Ks(request, rzaqks, 'rzaqks.html')

# 去入职测试考试界面
def Rzcsks_Views(request):
    # 生成10道单选题,10道多选,10道判断,10道填空,4道简答题
    return Ks(request, rzcsks, 'rzcsks.html', 10, 10, 10, 10, 4)

# 获取用户信息并跳转界面模板
def Information(request, html, mydict = None):
    try:
        uname = request.session.get('uname', '')
        ucompany = request.session.get('ucompany', '')
        udepartment1 = request.session.get('udepartment1', '')
        udepartment2 = request.session.get('udepartment2', '')
        upost = request.session.get('upost', '')
        mydict = mydict
        if uname:
            return render(request, html, locals())
        else:
            return HttpResponseRedirect('/')
    except Exception:
        return HttpResponseRedirect('/')


def Management_Views(request):
    return Information(request, 'personal_management.html')
# 安全考试选择页面跳转
def Aqks_Views(request):
    return Information(request, 'rzaqks_select.html')
# 入职考试选择页面跳转
def Rzcs_Views(request):
    return Information(request, 'rzcs_select.html')

def Maintain_Data_Views(request):
    try:
        question_type = request.GET.get('question_type', '')
        if question_type == '1':
            mydict = list(rzcsks.objects.filter(question_type='1').values())
            # 去往单选维护界面
            return Information(request, 'radio_data.html', mydict)
        elif question_type == '2':
            mydict = list(rzcsks.objects.filter(question_type='2').values())
            # 去往多选维护界面
            return Information(request, 'select_data.html', mydict)
        elif question_type == '3':
            mydict = list(rzcsks.objects.filter(question_type='3').values())
            # 去往判断维护界面
            return Information(request, 'judge_data.html', mydict)
        elif question_type == '4':
            mydict = list(rzcsks.objects.filter(question_type='4').values())
            # 去往填空维护界面
            return Information(request, 'completion_data.html', mydict)
        elif question_type == '5':
            mydict = list(rzcsks.objects.filter(question_type='5').values())
            # 去往简答维护界面
            return Information(request, 'short_answer_data.html', mydict)
        else:
            return HttpResponse('/')
    except Exception:
        return HttpResponse('/')

def SaveObject(request):
    # 保存题目
    datas = eval(request.GET.get('datas', ''))
    if datas:
        for mydata in datas:
            rzcsks.objects.create(question_type=mydata[0],
                                  subject=mydata[1],
                                  a_option=mydata[2],
                                  b_option=mydata[3],
                                  c_option=mydata[4],
                                  d_option=mydata[5],
                                  answer=mydata[6],
                                  )
        return HttpResponse(json.dumps({'msg': len(datas)}))
    else:
        return HttpResponse(json.dumps({'msg': '数据为空'}))

 # 删除题目
def DeleteData(request):
    mydata =eval(request.GET.get('mydata', ''))
    if mydata:
        rzcsks.objects.filter(id=mydata).delete()
        return HttpResponse(json.dumps({'msg': '删除成功'}))
    else:
        return HttpResponse(json.dumps({'msg': '删除失败'}))
# 选择
def Select_Object_Views(request):
    level = request.session.get('level', '')
    # 权限判定
    if level > 0:
        return Information(request, 'object_management.html')
    else:
        return HttpResponse('权限不足,请确认')

# 展示分数
def Show_Score_Views(request):
    level = request.session.get('level', '')
    # 权限判定
    if level>0:
        return Information(request, 'show_score.html')
    else:
        return HttpResponse('权限不足,请确认')
# 保存分数
def Save_Score_Views(request):
    # 获取session保存的登陆ID
    login_id = request.session.get('login_id', '')
    datas = eval(request.GET.get('datas', ''))
    u = list(rzcsks_score.objects.filter(login_id = login_id).values())
    if u:
        if not u[0]['second']:
            rzcsks_score.objects.filter(login_id = login_id).update(second = datas[1])
            return HttpResponse(json.dumps({'msg': '第二次成绩保存成功'}))
        else:
            if not u[0]['third']:
                rzcsks_score.objects.filter(login_id=login_id).update(third=datas[1])
                return HttpResponse(json.dumps({'msg': '第三次成绩保存成功'}))
            else:
                return HttpResponse(json.dumps({'msg': '您已完成三次成绩,无法提交'}))
    else:
        rzcsks_score.objects.create(login_id = login_id,
                                    first = datas[1],
                                    )

        return HttpResponse(json.dumps({'msg': '第一次成绩保存成功'}))

def Show_Select_Object_Views(request):
    # 引用考试类型
    datas = question_type
    return HttpResponse(json.dumps({'msg': datas}))

def Show_Select_Score_Views(request):
    # 获取题目类型
    qt = eval(request.GET.get('datas', ''))
    if qt[0] == 'rzaqks':
        return HttpResponse(json.dumps({'msg': '暂未开通'}))
    elif qt[0] == 'rzcsks':
        if not qt[1]:
            datas1 = list(rzcsks_score.objects.all().values())
            datas2 = list(login.objects.all().values())
            datas = [datas1, {}, '入职测试考试']
            for i in datas1:
                datas[1][i['login_id']] = find_login(i['login_id'], datas2)
            return HttpResponse(json.dumps({'msg': datas}))
        # 查询姓名
        elif qt[1][0] == 'u_name':
            datas = ''
            datas1 = list(login.objects.filter(u_name=qt[1][1]).values())
            if datas1:
                datas = [[], {}, '入职测试考试']
                for i in datas1:
                    myid = str(i['id'])
                    datas2 = list(rzcsks_score.objects.filter(login_id=myid).values())
                    if datas2:
                        for x in datas1:
                            id = datas2[0]['login_id']
                            if id == str(x['id']):
                                datas[0].append({'login_id': id,
                                                 'first': datas2[0]['first'],
                                                 'second': datas2[0]['second'],
                                                 'third': datas2[0]['third']})
                                datas[1][id] = [x['u_name'], x['u_phone']]
            return HttpResponse(json.dumps({'msg': datas}))
        # 查询手机号
        elif qt[1][0] == 'u_phone':
            datas = ''
            datas1 = list(login.objects.filter(u_phone=qt[1][1]).values())
            if datas1:
                datas = [[], {}, '入职测试考试']
                for i in datas1:
                    myid = str(i['id'])
                    datas2 = list(rzcsks_score.objects.filter(login_id=myid).values())
                    if datas2:
                        for x in datas1:
                            id = datas2[0]['login_id']
                            if id == str(x['id']):
                                datas[0].append({'login_id': id,
                                                 'first': datas2[0]['first'],
                                                 'second': datas2[0]['second'],
                                                 'third': datas2[0]['third']})
                                datas[1][id] = [x['u_name'], x['u_phone']]
            return HttpResponse(json.dumps({'msg': datas}))
        else:
            return HttpResponse(json.dumps({'msg': '数据异常'}))
    else:
        return  HttpResponse(json.dumps({'msg': '数据异常'}))

# 查找注册列表
def find_login(id,datas):
    for i in datas:
        if id == str(i['id']):
            return [i['u_name'], i['u_phone']]

def Updata_Score_Views(request):
    datas = eval(request.GET.get('datas', ''))
    datas1 = list(login.objects.filter(u_phone=datas[1]).values())
    if datas1:
        datas[1] = datas1[0]['id']
        if datas[0] == '入职测试考试':
            if datas[2] == 'first':
                if datas[3]:
                    rzcsks_score.objects.filter(login_id=datas[1]).update(first=datas[3])
                    return HttpResponse(json.dumps({'msg': '第三次分数为{}'.format(datas[3])}))
                else:
                    return HttpResponse(json.dumps({'msg': '保存失败'}))
            elif datas[2] == 'second':
                if datas[3]:
                    rzcsks_score.objects.filter(login_id=datas[1]).update(second=datas[3])
                    return HttpResponse(json.dumps({'msg': '第三次分数为{}'.format(datas[3])}))
                else:
                    return HttpResponse(json.dumps({'msg': '保存失败'}))
            elif datas[2] == 'third':
                if datas[3]:
                    rzcsks_score.objects.filter(login_id=datas[1]).update(third=datas[3])
                    return HttpResponse(json.dumps({'msg': '第三次分数为{}'.format(datas[3])}))
                else:
                    return HttpResponse(json.dumps({'msg': '保存失败'}))
        elif datas1[0] == '入职安全考试':
            return HttpResponse(json.dumps({'msg': '暂未开通'}))
        else:
            return HttpResponse(json.dumps({'msg': '保存失败'}))
    print(datas)
    return HttpResponse(json.dumps({'msg': '保存失败'}))