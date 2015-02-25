# -*- coding: cp936 -*-
from bs4 import BeautifulSoup
import urllib2,urllib,json,re,codecs

content=urllib2.urlopen('http://aqicn.org/city/all/cn/',timeout=100).read()
soup = BeautifulSoup(content)
stations = {}
for i in soup.find('div',text=u'中国').next_sibling.find_all('a',{'href':re.compile('^http://aqicn.org/city/')}):
    link = i.get('href') + 'm/'
    stations[link] = i.text
print len(stations)
outfile = codecs.open('stations.txt','w','utf-8')
stations_write = json.dumps(stations,ensure_ascii=False)
outfile.write(stations_write)
outfile.close()
