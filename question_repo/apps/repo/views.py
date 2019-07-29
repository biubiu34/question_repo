from django.shortcuts import render ,HttpResponse

import logging

def test(request):
    return HttpResponse("题库视图")