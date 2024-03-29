# -*- coding: utf-8 -*-
import hashlib
from django.db import models
from django.core.cache import cache
from datetime import date, datetime, timedelta

CACHE_KEY_GIFT_CODE = 'cach_gift_code_%s' #%s is gift_code
CACHE_KEY_GIFT_CODE2 = 'cach_gift_code_r_%s' #%s is md5(receipt )
CACHE_KEY_GIFT_CODES = 'cach_gift_code_u_%s' #%s is uid 
CACHE_KEY_GIFT_CODE_RECODE = 'cach_gift_code_record_%s' #%s is gift_code

class GiftCode(models.Model):
    uid = models.CharField(max_length=100)
    receipt = models.TextField(max_length=10000)
    type = models.CharField(max_length=10)
    gift_code = models.CharField(max_length=32,blank=True,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    used_info = models.TextField(blank=True,null=True, max_length=1000)
    
    def update_cache(self):
        key = CACHE_KEY_GIFT_CODE % (self.gift_code)
        cache.set(key, self)
        key = CACHE_KEY_GIFT_CODE2 % (hashlib.md5(self.receipt).hexdigest())
        cache.set(key, self)
        
    def delete_cache(self):
        key = CACHE_KEY_GIFT_CODE % (self.gift_code)
        cache.delete(key)
        key = CACHE_KEY_GIFT_CODE2 % (hashlib.md5(self.receipt).hexdigest())
        cache.delete(key)
        
    def save(self):
        super(GiftCode, self).save()
        self.update_cache()
        
    def delete(self):
        self.delete_cache()
        super(GiftCode, self).delete()
    
    class Meta:
        db_table = 'ios_giftcode'


class GiftCodeRecord(models.Model):
    uid = models.CharField(max_length=100)
    gift_code = models.CharField(max_length=32)
    platforms = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def update_cache(self):
        key = CACHE_KEY_GIFT_CODE_RECODE % (self.gift_code)
        cache.set(key, self)
        
    def delete_cache(self):
        key = CACHE_KEY_GIFT_CODE_RECODE % (self.gift_code)
        cache.delete(key)
        
    def save(self):
        super(GiftCodeRecord, self).save()
        self.update_cache()
        
    def delete(self):
        self.delete_cache()
        super(GiftCodeRecord, self).delete()
    
    class Meta:
        db_table = 'ios_giftcoderecord'

