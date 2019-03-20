from django.shortcuts import render
def index(request):
	context_dict = {'boldmessage': "Fun, happiness, joy!"}
	return render(request, 'gamezone/index.html', context=context_dict)

def about(request):
	return render(request, 'gamezone/about.html')