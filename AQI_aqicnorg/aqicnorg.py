POST_URL="http://10.50.6.70:8080/data/write"
POST_NAME="AQICN"

from bs4 import BeautifulSoup
import json,re,cookielib,time,datetime,sys,requests

reload(sys)
sys.setdefaultencoding('utf8') 

def getpage(link):
    r = s.get(link)
    content=r.content
    if r.status_code == 503:
        content = getpage(link)
    return content

def getdata(content):
    soup = BeautifulSoup(content)
    table = soup.find('table', 'aqigraphtable')
    stationdata = {}
    for i in range(len(vmap)):
        tr = 'tr_' + vmap[i]
        cur = 'cur_' + vmap[i]
        try:
            stationdata[tmap[i]] = table.find('tr', id = tr).find('td', id = cur).text
        except:
            stationdata[tmap[i]] = '-'
    return stationdata

def parse(link):
    try:
        print link
        content = getpage(link)
    except Exception as err:
        print "(failed)"+str(err)
        logFile.write("(failed)"+str(err)+"\n")
        time.sleep(5)
        content = getpage(link)
    stationdata = getdata(content)
    stationsdata[stations[link]] = stationdata
    print stations[link]
    print stationdata

logFile = open("aqicn.log", 'a')
logFile.write(datetime.datetime.fromtimestamp(time.time()).strftime("\n----%Y-%m-%d %H:%M:%S----\n"))
stations = json.loads(open("stations.txt",'r').read())
vmap = ['pm25','co','pm10','o3','so2','no2']
tmap = ["PM2_5","CO","PM10","O3","SO2","NO2"]
stationsdata = {}
s = requests.Session()
for link in stations:
    parse(link)
    
outfile = open("data.txt",'w')
jsonCoded=json.dumps(stationsdata, ensure_ascii=False)
outfile.write(jsonCoded)
postDict = {"content":jsonCoded,"key":POST_NAME}
resp = requests.post(POST_URL,data=postDict)
logFile.write("Response:"+resp.content+"\n")
print resp.content

logFile.close()
resp.close()
outfile.close()
