from django.shortcuts import render

# Create your views here.


def filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'hello! Django','dt':dt,'c':4}
    return render(request,'filters.html',d)