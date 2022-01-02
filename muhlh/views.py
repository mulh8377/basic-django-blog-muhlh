from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	context = {
		'text': "hello",
		'sound': "beep",
		'photos': 'yikes',
	}

	return render(request, 'index.html', context=context)


# Create your views here.
