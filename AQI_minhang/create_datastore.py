from ckanapi import *

resource_id = "a17b07fb-43a8-4705-a435-7624d497baf4"
api_key = "ee6c2082-bd9f-421b-9455-07520c9108ff"

# create the datastore for your resource and update the url
datastore_create(resource_id, api_key)
url_update(resource_id, api_key)
