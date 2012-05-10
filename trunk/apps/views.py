# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.helper import *
from apps.cache import *


def index(request):
    type = request.GET.get('type')
    if type == 'ip3gs':
        return render_to_response('ip3.html')
    else:
        return HttpResponseRedirect('ip4.html')

def ad(request):
    type = request.GET.get('type')
    if type == 'ip3gs':
        return HttpResponseRedirect('/media/ios/ad02.jpg')
    else:
        return HttpResponseRedirect('/media/ios/ad01.jpg')