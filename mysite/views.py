from django.shortcuts import render
from django.http import HttpResponse
import random, datetime
from mysite import models
from django.template import RequestContext
from http import HTTPStatus

#from flask import Flask, redirect, url_for, render_template,request

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
def index(request):
	posts = models.Post.objects.all()	
	return render(request, "index.html", locals())

def lotto(request):
	numbers = [n for n in range(1, 43)]
	random.shuffle(numbers)
	lotto = numbers[:6]
	special = numbers[6]
	return render(request, "lotto.html", locals())
 
def date(request):

	posts = models.Post.objects.all()	

	now = datetime.datetime.now()
	#return HttpResponse("現在時刻 : {}".format(now))
	return render(request, "date.html", locals())

def mail(request):

	return render(request, "mail.html", locals())

def play(request):

	return render(request, "play.html", locals())

def play1(request):

	return render(request, "play1.html", locals())

def play2(request):

	return render(request, "play2.html", locals())

def play3(request):

	return render(request, "play3.html", locals())

def play4(request):

	return render(request, "play4.html", locals())

def play5(request):

	return render(request, "play5.html", locals())

def mom(request):
	
	return render(request, "mom.html", locals())

def index1(request):
	
	return render(request, "index1.html", locals())

def index2(request):
	
	return render(request, "index2.html", locals())

def index3(request):
	
	return render(request, "index3.html", locals())

def passfirst(request):

	return render(request, "passfirst.html", locals())

def passsecond(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = NameForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        password = request.POST["inputPassword2"]
        #sss = request.POST.get('inputPassword2')
    if password == '0224':
        return render(request,"mom.html",locals())

    # if a GET (or any other method) we'll create a blank form
    else:
        #form = NameForm()
       # return render(request,"lotto.html",locals())
    	return render(request,"passfirst.html",locals()) 

def passfourth(request):
	
	return render(request, "passfourth.html", locals())

def passthird(request):
	
	return render(request, "passthird.html", locals())

