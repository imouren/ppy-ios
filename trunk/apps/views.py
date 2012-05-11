# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from apps.helper import *
from apps.cache import *


def index(request):
    type = request.GET.get('type')
    receipt = request.GET.get('receipt')
    uid = request.GET.get('uid')
    if type == 'ipad':
        return render_to_response('ipad.html')
    else:
        return render_to_response('iphone.html')

def ad(request):
    type = request.GET.get('type')
    if type == 'ipad':
        return HttpResponseRedirect('/media/ios/ipad.png')
    else:
        return HttpResponseRedirect('/media/ios/iphone.png')

