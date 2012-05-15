# -*- coding: utf-8 -*-

import random
import copy
import time
import urllib
import urllib2
import hashlib
import base64
from datetime import date, datetime, timedelta
from django.utils import simplejson
from apps.models import *
from apps.cache import *

#APPLE_URL = 'https://buy.itunes.apple.com/verifyReceipt'
APPLE_URL = 'https://sandbox.itunes.apple.com/verifyReceipt' # for test

def get_or_create_gift_code(receipt, uid, type):
    gift_code = get_gift_code_by_receipt(receipt)
    if not gift_code:
        if verify_receipts(receipt):
            gift_code = hashlib.md5(receipt+str(time.time())).hexdigest()
            gift_code = GiftCode(
                        receipt = receipt,
                        uid = uid, 
                        type = type, 
                        gift_code = gift_code
                        )
            gift_code.save()
    return gift_code

def verify_receipts(receipts):
    data = simplejson.dumps({"receipt-data" : receipts})
    req = urllib2.Request(APPLE_URL, data, {'Content-Type': 'application/json'})
    result = urllib2.urlopen(req).read()
    print result
    res = simplejson.loads(result)
    if res['status'] == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    #receipts = 'Y29tLnVydXMuaWFwLjIyMjkwNDQw'
    receipts = "ewoJInNpZ25hdHVyZSIgPSAiQXJrYkNKdXFyL3RYbG9pMWJmWnl6NlRjZVpJN2JTenlzM3dDMDBLQjN3RHg2MVV0ZnBBdVBFZHFkdTVaY2pQeFYvbkRiTktLWXkwOTAySGVsMkRlSEpnSzNJcVRPVWo1c2R4VzBzMU4wNVFlSU5ibVR3RHNKWEZKeDFHeTVLVUxYaUd2aFJSWTExcFBvZEg5dE55WVE2eW9mMWVRSEhlOUFMSmNBN20xc3BkakFBQURWekNDQTFNd2dnSTdvQU1DQVFJQ0NHVVVrVTNaV0FTMU1BMEdDU3FHU0liM0RRRUJCUVVBTUg4eEN6QUpCZ05WQkFZVEFsVlRNUk13RVFZRFZRUUtEQXBCY0hCc1pTQkpibU11TVNZd0pBWURWUVFMREIxQmNIQnNaU0JEWlhKMGFXWnBZMkYwYVc5dUlFRjFkR2h2Y21sMGVURXpNREVHQTFVRUF3d3FRWEJ3YkdVZ2FWUjFibVZ6SUZOMGIzSmxJRU5sY25ScFptbGpZWFJwYjI0Z1FYVjBhRzl5YVhSNU1CNFhEVEE1TURZeE5USXlNRFUxTmxvWERURTBNRFl4TkRJeU1EVTFObG93WkRFak1DRUdBMVVFQXd3YVVIVnlZMmhoYzJWU1pXTmxhWEIwUTJWeWRHbG1hV05oZEdVeEd6QVpCZ05WQkFzTUVrRndjR3hsSUdsVWRXNWxjeUJUZEc5eVpURVRNQkVHQTFVRUNnd0tRWEJ3YkdVZ1NXNWpMakVMTUFrR0ExVUVCaE1DVlZNd2daOHdEUVlKS29aSWh2Y05BUUVCQlFBRGdZMEFNSUdKQW9HQkFNclJqRjJjdDRJclNkaVRDaGFJMGc4cHd2L2NtSHM4cC9Sd1YvcnQvOTFYS1ZoTmw0WElCaW1LalFRTmZnSHNEczZ5anUrK0RyS0pFN3VLc3BoTWRkS1lmRkU1ckdYc0FkQkVqQndSSXhleFRldngzSExFRkdBdDFtb0t4NTA5ZGh4dGlJZERnSnYyWWFWczQ5QjB1SnZOZHk2U01xTk5MSHNETHpEUzlvWkhBZ01CQUFHamNqQndNQXdHQTFVZEV3RUIvd1FDTUFBd0h3WURWUjBqQkJnd0ZvQVVOaDNvNHAyQzBnRVl0VEpyRHRkREM1RllRem93RGdZRFZSMFBBUUgvQkFRREFnZUFNQjBHQTFVZERnUVdCQlNwZzRQeUdVakZQaEpYQ0JUTXphTittVjhrOVRBUUJnb3Foa2lHOTJOa0JnVUJCQUlGQURBTkJna3Foa2lHOXcwQkFRVUZBQU9DQVFFQUVhU2JQanRtTjRDL0lCM1FFcEszMlJ4YWNDRFhkVlhBZVZSZVM1RmFaeGMrdDg4cFFQOTNCaUF4dmRXLzNlVFNNR1k1RmJlQVlMM2V0cVA1Z204d3JGb2pYMGlreVZSU3RRKy9BUTBLRWp0cUIwN2tMczlRVWU4Y3pSOFVHZmRNMUV1bVYvVWd2RGQ0TndOWXhMUU1nNFdUUWZna1FRVnk4R1had1ZIZ2JFL1VDNlk3MDUzcEdYQms1MU5QTTN3b3hoZDNnU1JMdlhqK2xvSHNTdGNURXFlOXBCRHBtRzUrc2s0dHcrR0szR01lRU41LytlMVFUOW5wL0tsMW5qK2FCdzdDMHhzeTBiRm5hQWQxY1NTNnhkb3J5L0NVdk02Z3RLc21uT09kcVRlc2JwMGJzOHNuNldxczBDOWRnY3hSSHVPTVoydG04bnBMVW03YXJnT1N6UT09IjsKCSJwdXJjaGFzZS1pbmZvIiA9ICJld29KSW5GMVlXNTBhWFI1SWlBOUlDSXhJanNLQ1NKd2NtOWtkV04wTFdsa0lpQTlJQ0pVZFhKcGMzUnBYek0wWHpJelh6QTVYekl3TVRFaU93b0pJbWwwWlcwdGFXUWlJRDBnSWpRME1qWTVNVGczTnlJN0Nna2lkbVZ5YzJsdmJpMWxlSFJsY201aGJDMXBaR1Z1ZEdsbWFXVnlJaUE5SUNJek5EazROVFV4SWpzS0NTSndkWEpqYUdGelpTMWtZWFJsSWlBOUlDSXlNREV4TFRFd0xUQXlJREEzT2pNeU9qVXlJRVYwWXk5SFRWUWlPd29KSW1Gd2NDMXBkR1Z0TFdsa0lpQTlJQ0l6TnpNM056STNNamdpT3dvSkluUnlZVzV6WVdOMGFXOXVMV2xrSWlBOUlDSXlNekF3TURBd01ERTJNREV3TXpFaU93b0pJbTl5YVdkcGJtRnNMWEIxY21Ob1lYTmxMV1JoZEdVaUlEMGdJakl3TVRFdE1UQXRNRElnTURjNk16STZOVElnUlhSakwwZE5WQ0k3Q2draWIzSnBaMmx1WVd3dGRISmhibk5oWTNScGIyNHRhV1FpSUQwZ0lqSXpNREF3TURBd01UWXdNVEF6TVNJN0Nna2lZbWxrSWlBOUlDSmpiMjB1Y0dGd1pYSnNhWFF1YVhCaFpDNTBkWEpwYzNScGNHVnlZMkZ6YnpJaU93b0pJbUoyY25NaUlEMGdJalF1TWlJN0NuMD0iOwoJInBvZCIgPSAiMjMiOwoJInNpZ25pbmctc3RhdHVzIiA9ICIwIjsKfQ=="
    print len(receipts)
    print verify_receipts(receipts)
