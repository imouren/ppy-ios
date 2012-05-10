# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.helper import *
from apps.cache import *


def index(request):
    return HttpResponse('have a look.')

def ad(request):
    type = request.GET.get('type')
    if type == 'iphone3':
        return HttpResponseRedirect('/media/ad02.jpg')
    else:
        return HttpResponseRedirect('/media/ad01.jpg')