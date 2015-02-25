# -*- coding: utf-8 -*-

# your resource_id and api_key
resource_id = 'a17b07fb-43a8-4705-a435-7624d497baf4'
api_key = 'ee6c2082-bd9f-421b-9455-07520c9108ff'

import requests
import json
import time,datetime
import sys
import ckanapi
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

try:
	logFile = open("minhangaqi.log", 'a')
	logFile.write(datetime.datetime.fromtimestamp(time.time()).strftime("\n----%Y-%m-%d %H:%M:%S----\n"))
	content=requests.get("http://116.236.251.22/aqi/Station.aspx").content
	soup=BeautifulSoup(content)
	dataList=[]
	table=soup.find("tbody").find_all("tr")
	for row in table:
		dataRow={}
		column = row.find_all("td")
		dataRow["station"] = column[0].text
		dataRow["PM2_5"] = column[1].text
		dataRow["O3"] = column[2].text
		dataRow["CO"] = column[3].text
		dataRow["PM10"] = column[4].text
		dataRow["SO2"] = column[5].text
		dataRow["NO2"] = column[6].text
		dataRow["datetime"] = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")
		dataList.append(dataRow)
	ckanapi.datastore_upsert(resource_id, dataList, api_key)
except Exception as err:
    print err
    logFile.write(str(err)+"\n")
finally:
    logFile.close()