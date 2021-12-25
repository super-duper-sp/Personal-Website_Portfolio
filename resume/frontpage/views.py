from django.shortcuts import render
from .models import MAINpageContent

def landingpage(request):
    return render(request,'landingpage.html')

def frontpage(request):
    main = MAINpageContent.objects.filter()
    return render(request, 'frontpage.html', {'main': main})


