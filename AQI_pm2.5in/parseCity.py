from bs4 import BeautifulSoup
import urllib2,urllib,json,sys

reload(sys)
sys.setdefaultencoding('utf8') 

content=urllib2.urlopen('http://pm25.in',timeout=100).read()
soup = BeautifulSoup(content)
cities = soup.find("div","all").find_all('a')
city_info = {}
for city_element in cities:
    pinyin = city_element.get('href')[1:]
    name = city_element.text
    baiduMapUrl = "http://api.map.baidu.com/geocoder/v2/?output=json&ak=RhLNCiOOt5YZKxD0XPBWuUFT&address=" + name
    baiduMapResponse = urllib2.urlopen(baiduMapUrl)            
    baiduMapObj = json.loads(baiduMapResponse.read())
    city={}
    city['name'] = name
    city['lng'] = baiduMapObj['result']['location']['lng']
    city['lat'] = baiduMapObj['result']['location']['lat']
    city_info[pinyin] = city

outfile = open('cities.txt','w')
cities_write = json.dumps(city_info,ensure_ascii=False)
outfile.write(cities_write)
outfile.close()
