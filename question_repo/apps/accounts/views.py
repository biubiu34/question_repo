from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("帐户视图")