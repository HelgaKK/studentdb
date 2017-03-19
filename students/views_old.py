from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Views for Students
def students_list(request):
    students = (
        {'id':1, 'first_name':u'Виталий', 'last_name':u'Подоба',
         'ticket':235, 'image':"img/dressing2.jpg"},
        {'id': 2, 'first_name': u'Андрей', 'last_name': u'Добопа',
         'ticket': 457, 'image': "img/dressing3.jpg"},
        {'id': 3, 'first_name': u'Семен', 'last_name': u'Иванов',
         'ticket': 678, 'image': "img/dressing4.jpg"},
    )
    return render(request,'students/students_list.html', {'students':students})

def students_add(request):
    return HttpResponse('<h1>Add student form</h1>')

def students_edit(request,sid):
    return HttpResponse('<h1>Edit student %s</h1>' % sid)

def students_delete(request,sid):
    return HttpResponse('<h1>delete student %s</h1>' % sid)

# Views for Journal
def journal(request):

    return render(request, 'students/journal.html')
def journal_student(request):
    return HttpResponse('<h1>to see student journal</h1>')
def journal_update(request):
    return HttpResponse('<h1>journal update/h1>')
# Views for Groups

def groups_list(request):
    leader = ({'leaderid':11, 'leadername':u'Подоба Виталий'},
              {'leaderid':21, 'leadername':u'Иванов Иван'},
              {'leaderid':31,'leadername':u'Андреев Андрей'},
              )
    groups = (
        {'id': 1, 'name': u'МТБ-11', 'leader': leader[0],},
        {'id': 2, 'name': u'МТБ-12', 'leader': leader[1],},
        {'id': 3, 'name': u'МТБ-13', 'leader': leader[2],},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group add form</h1>')
def groups_edit(request,gid):
    return HttpResponse('<h1>Edit group %s</h1>' % gid)

def groups_delete(request,gid):
    return HttpResponse('<h1>delete group %s</h1>' % gid)