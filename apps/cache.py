# -*- coding: utf-8 -*-

import cPickle
import sys
from django.core.cache import cache
from apps.models import *

def get_gift_code(gift_code):
    key = CACHE_KEY_GIFT_CODE % (gift_code)
    obj = cache.get(key)
    
    if obj is None:
        try:
            obj = GiftCode.objects.get(gift_code=gift_code)
            cache.set(key, obj)
        except:
            obj = None
    return obj

def get_gift_code_by_receipt(receipt):
    key = CACHE_KEY_GIFT_CODE2 % (hashlib.md5(receipt).hexdigest())
    obj = cache.get(key)
    
    if obj is None:
        try:
            obj = GiftCode.objects.get(receipt=receipt)
            cache.set(key, obj)
        except:
            obj = None
    return obj

def get_gift_codes_by_uid(uid):
    obj = GiftCode.objects.filter(uid=uid)
    return obj