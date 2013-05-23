from django.http import HttpResponse

def hello(request):
	return HttpResponse("Helloword, this is Scott.")