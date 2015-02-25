# -*- coding: utf-8 -*-

from ckanapi import *

resource_id = "4c75acdf-4f76-4b58-adc7-b3d11a5ba5c9"
api_key = "00d9892e-38d3-40ba-ae61-e132ed29c57b"

data={"station":"Xinjiekou"}

datastore_delete(resource_id, data, api_key)
 