from django.shortcuts import render
from django.http import HttpResponse
import random, datetime
from mysite import models
 
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

	now = datetime.datetime.now()
	#return HttpResponse("現在時刻 : {}".format(now))
	return render(request, "date.html", locals())

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

def passfirst(request):
	
	return render(request, "passfirst.html", locals())

def passsecond(request):
	
	return render(request, "passsecond.html", locals())

def passfourth(request):
	
	return render(request, "passfourth.html", locals())

def passthird(request):
	
	return render(request, "passthird.html", locals())