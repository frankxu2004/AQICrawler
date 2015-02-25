POST_URL="http://202.121.178.214:8080/data/write"
POST_NAME="PM25"

import requests
import json
import time,datetime
import sys

reload(sys)
sys.setdefaultencoding('utf8') 

try:
    logFile = open("pm25in.log", 'a')
    logFile.write(datetime.datetime.fromtimestamp(time.time()).strftime("\n----%Y-%m-%d %H:%M:%S----\n"))
    cities_json = open("cities.txt", 'r').read().decode('utf-8')
    cities = json.loads(cities_json)
    jsonObj = {}
    res_all = []
    s = requests.Session()
    for pinyin in cities:
	print cities[pinyin]['name']
        url1 = "http://www.pm25.in/api/querys/aqi_details.json?city="+pinyin+"&token=5j1znBVAsnSf5xQyNQyq"
        url2 = "http://www.pm25.in/api/querys/aqi_details.json?city="+pinyin
        response = s.get(url1)
	print response.content
        jsonObj = json.loads(response.content)
        response.close()
        vmap=["pm2_5","co","pm10","o3","so2","no2"]
        tmap=["PM2_5","CO","PM10","O3","SO2","NO2"]
        res = {}
        res['city']=cities[pinyin]['name']
        res['location']={}
        res['location']['lng']=cities[pinyin]['lng']
        res['location']['lat']=cities[pinyin]['lat']
        res['stations']=[]
        for station in jsonObj:
            stationdata={}
            stationdata['data']={}
            if(station['position_name']!=None):
                stationdata['name']=station['position_name']
                for i in range(len(vmap)):
                    stationdata['data'][tmap[i]]=station[vmap[i]]
            else:    
                stationdata['name']='Average'
                for i in range(len(vmap)):
                    stationdata['data'][tmap[i]]=station[vmap[i]]
            res['stations'].append(stationdata)
        res_all.append(res)
    outfile = open("data.txt","w")
    jsonCoded=json.dumps(res_all,ensure_ascii=False)
    outfile.write(jsonCoded)
    postDict = {"content":jsonCoded,"key":POST_NAME}
    resp = requests.post(POST_URL,data=postDict)
    logFile.write("Response:"+resp.content+"\n")
    print resp.content
except Exception as err:
    print err
    logFile.write(str(err)+"\n")
finally:
    logFile.close()
    resp.close()
    outfile.close()
