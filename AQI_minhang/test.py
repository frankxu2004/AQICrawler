# -*- coding: utf-8 -*-

from ckanapi import *

resource_id = "519e34eb-920d-4215-a634-a47832e03cf6"
api_key = "268016bf-92cd-48ca-8406-3ad2f1528c1b"

data=[{"date":"Fri Oct 03 21:35:31 GMT+08:00 2014","mac_address":"B4:99:4C:64:CF:06","sensor_uuid":"f000aa20-0451-4000-b000-000000000000","value":"46.773327"}]
datastore_upsert(resource_id, data, api_key)
