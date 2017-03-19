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