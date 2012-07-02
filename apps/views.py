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
    gift_codes = list(gift_codes)
    gift_records = get_gift_code_records_by_uid(uid)
    for g in gift_codes:
        if g.gift_code in gift_records:
            gift_codes.remove(g)
    left_div = []
    if gift_codes:
        left_num = 0 if len(gift_codes)>3 else 3-len(gift_codes)
        left_div = [i for i in range(left_num)]
    data = {'gift_codes':gift_codes, 'have_gift_code':gift_codes is not None and len(gift_codes)>0, 'left_div':left_div}
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


def exchange_gift(request):
    gift_code = request.GET.get('gift_code', '') or request.POST.get('gift_code', '')
    platforms = request.GET.get('platforms', '') or request.POST.get('platforms', '')
    sig = request.GET.get('sig', '') or request.POST.get('sig', '')
    mysig = new_sig(gift_code, platforms)
    
    data = None
    
    if sig != mysig:
        data = {'error':'sig error'}

    key = "lock_iphone_gift_%s" %(gift_code)
    locked = cache.get(key)
    if locked:
        return {'error':'gift_code error'}
    else:
        cache.set(key, True, 30)

    gift_code_obj = get_gift_code(gift_code)
    if not gift_code_obj:
        data = {'error':'gift code does not exist'}

    gift_code_recode_obj = get_gift_code_recode(gift_code)
    if gift_code_recode_obj:
        data = {'error':'gift code have used'}

    if not data:
        gift_code_record = GiftCodeRecord(
                    uid = gift_code_obj.uid,
                    gift_code = gift_code,
                    platforms = platforms, 
                    )
        gift_code_record.save()
        data = {'ok':'ok'}

    response = HttpResponse(simplejson.dumps(data))
    response['Content-type'] = 'application/json'
    return response
