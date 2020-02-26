from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def qsMethodCalled(request):

    return HttpResponse("haha, you must like cat as me. Miao~")

# using shortcuts.render() method instead of HttpResponse() method

#     render(req, 'html.file', locals())

# the 1st param means http request in GET | POST method

# the 2nd param is a templates file name in string type.

# the 3rd param is callback of locals() method, to pass local variables

#        locals()

def renderMiao(request, user_name):

    time_now = datetime.now()

    return render(request, "miao.html", locals())

def renderPoupou(request):
    
    return render(request, "poupou.html")

def renderPhoto(request):

    return render(request, "showmephoto.html", locals())

def renderTime(request):

    time_now = datetime.now()
    return render(request, 'showclocktime.html', locals())
