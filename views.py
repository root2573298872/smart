from django.http import HttpResponse
def index(request):
    return HttpResponse('ok')
def login(request):
    return HttpResponse('ok2')

