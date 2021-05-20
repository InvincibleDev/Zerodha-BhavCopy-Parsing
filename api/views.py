import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone

# Create your views here.

redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)

@api_view(["GET"])
def getHeadScrips(request):
    '''
    input : ""
    output: Data of 10 scrips from the Redis Store

    Response status : 1 indicates Success,
                    : 0 indictes Error
    '''
    result={}
    all_scrips = redis_instance.keys("*")
    scrip_keys = [name.decode('utf-8') for name in all_scrips]
    for scrip_name in all_scrips[:10]:
        stored_data = redis_instance.lrange(scrip_name,0,redis_instance.llen(scrip_name))
        result[scrip_name.decode("utf-8")] = json.loads(stored_data[0])
    response = {
                "status": 1,
                "result":result,
                "scrip_keys":scrip_keys
    }
    return Response(response, status = 200)

@api_view(["GET"])
def searchScrip(request, scrip_name):
    '''
    input : "scrip_name which is the search string"
    output: Data of "scrip_name" from the Redis Store

    Response status : 1 indicates Success,
                    : 0 indictes Error
    '''
    result = {}
    stored_data = redis_instance.lrange(scrip_name,0,redis_instance.llen(scrip_name))
    if not len(stored_data):
        return Response({
                         "status":"0", # O status indictes error
                         "message":"Scrip Name Does Not Exist"
        })
    result[scrip_name] = []
    for data in stored_data:
        result[scrip_name].append(json.loads(data))
    response = {
            "status": 1,
            "result":result
    }
    return Response(response, status = 200)
