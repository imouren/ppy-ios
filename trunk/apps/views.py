# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from apps.helper import *
from apps.cache import *


def index(request):
    type = request.GET.get('type', 'ipad')
    receipt = request.GET.get('receipt')
    uid = request.GET.get('uid')
    if receipt and uid:
        gift_code = get_or_create_gift_code(receipt, uid, type)
    gift_codes = get_gift_codes_by_uid(uid)
    left_num = 0
    if gift_codes:
        left_num = 0 if len(gift_code)>3 else 3-len(gift_code)
        left_div = [i for i in range(left_num)]
    data = {'gift_codes':gift_codes, 'have_gift_code':gift_codes is not None and len(gift_codes)>0, 'left_idv':left_div}
    if type == 'ipad':
        return render_to_response('ipad.html', data, context_instance=RequestContext(request))
    else:
        return render_to_response('iphone.html', data, context_instance=RequestContext(request))

def ad(request):
    type = request.GET.get('type')
    if type == 'ipad':
        return HttpResponseRedirect('/media/ios/ipad_tw.png')
    else:
        return HttpResponseRedirect('/media/ios/iphone_tw.png')

