#!/usr/bin/env python
from bottle import route, run, template, request, response
import json
from sxgeo import SxAPI

@route('/ip/')
def index():
    response.content_type = 'application/json; charset=utf-8'
    try:
	ip=request.query.ip
    except:
        return "{'error':'empty ip'}"
    try:
       flog.write(" "+ip+"\n")
    except:
       pass # No ochen loho
    arr={}
    arr['ip']=ip
    iploc = api.locate(ip)
    arr['country_id'] = iploc.country_id
    arr['id'] = iploc.id
    arr['lat'] = iploc.lat
    arr['lon'] = iploc.lon
    arr['name_en'] = iploc.name_en
    arr['name_ru'] = iploc.name_ru
    arr['region_seek'] = iploc.region_seek
    s = json.dumps(arr)
    if (request.query.callback):
        s = request.query.callback+"("+s+")"
    return s
flog = open('ips','a')
api = SxAPI('../bash_get/SxGeoCity.dat')
run(host='127.0.0.1', port=5001,server='paste') #server='paste'