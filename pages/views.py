from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title': 'Index page',
		'name': 'CodeLag',
	}
	return render(request, 'pages/index.html', context)
