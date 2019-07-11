from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import News,Python,Api,Html,Search
from .forms import Newsletter,Pythonform,Apiform,Htmlform,Searchform

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
from email.mime.image import MIMEImage
from django.http import JsonResponse
import json

from django.db.models import Q
from django.http import Http404
from django.http import *
from django.contrib import messages


def home(request):
    return render(request, 'index.html')

def newsletter(request):
    email=request.POST.get('a8')
    f=News(Email=email)
    f.save()
    subject, from_email,recipient_list = 'Durga-soft institute latest updates', 'settings.EMAIL_HOST_USER',[f.Email]
    text_content = 'This is an important message ....'
    html_content = '<h3><p>Thank you for Subscribing ...for futher updates we will contact u as soon as possible..</p></h3>'
    msg = EmailMultiAlternatives(subject, text_content, from_email,recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return render(request,'courses.html')

def courses(request):
    return render(request, 'courses.html')

def python(request):
    if request.method == "POST":
        fform=Pythonform(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            message=request.POST.get('message')
            data=Python(
                name=name,
                email=email,
                phone=phone,
                message=message
                )
            data.save()
            fform=Pythonform()
            fdata = Python.objects.all()
            return render(request,'sucess.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = Pythonform()
        fdata = Python.objects.all()
    return render(request, 'python.html',{'fform': fform,'fdata': fdata})

def api(request):
    if request.method == "POST":
        fform=Apiform(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            message=request.POST.get('message')
            data=Api(
                name=name,
                email=email,
                phone=phone,
                message=message
                )
            data.save()
            fform=Apiform()
            fdata = Api.objects.all()
            return render(request,'sucess.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = Apiform()
        fdata = Api.objects.all()
    return render(request, 'api.html',{'fform': fform,'fdata': fdata})




def html(request):
    if request.method == "POST":
        fform=Htmlform(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            message=request.POST.get('message')
            data=Html(
                name=name,
                email=email,
                phone=phone,
                message=message
                )
            data.save()
            fform=Htmlform()
            fdata = Html.objects.all()
            return render(request,'sucess.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = Htmlform()
        fdata = Html.objects.all()
    return render(request, 'html.html',{'fform': fform,'fdata': fdata})


def sucess(request):
    return render(request, 'sucess.html')
def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch!=None:
            t = srch.split(",")
            l = []
            for i in t:
                print(i)
                match = Search.objects.filter(
                    Q(course__icontains=i) | Q(faculty__icontains=i) | Q(location__icontains=i))
                print(match)
                if match:
                    l.append(match)
                # print(l)
                else:
                    messages.error(request, 'data not found Please enter course name .......')

            # if len(l)==0:
            #     messages.error(request, 'no result found')
            # else:
            return render(request, 'search.html', {'sr':l})
        else:
            messages.sucess("enter data")
    else:
        #return HttpResponseRedirect('/search/')
        return render(request, 'search.html')