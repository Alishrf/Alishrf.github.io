from django.shortcuts import render


def index(request):
    a = 2
    context = {
        'a': a ,
    }
    return render(request,'index.html',context)