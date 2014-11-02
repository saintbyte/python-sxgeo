#!/usr/bin/env python
from bottle import route, run, template, request, response
import json
from sxgeo import SxAPI

@route('/ip/')
def index():
    response.content_type = 'application/json; charset=utf-8'
    ip=request.query.ip
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

api = SxAPI('../bash_get/SxGeoCity.dat')
run(host='0.0.0.0', port=5001,server='paste') #server='paste'