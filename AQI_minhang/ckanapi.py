import requests
import json
import pprint

def request(resource_dict,action_name,api_key):
	url = 'http://202.121.178.214/api/3/action/' + action_name
	print url
	print resource_dict
	print json.dumps(resource_dict)
	r = requests.post(url, data=json.dumps(resource_dict), headers={'Authorization':api_key,'content-type': 'application/json'})
	#assert r.status_code == 200
	print r.status_code
	print r.text
	response_dict = json.loads(r.text)
	print response_dict
	assert response_dict['success'] is True

	result = response_dict['result']
	return result

def datastore_create(resource_id,api_key):
	# create a datastore for a resource
	resource_dict = {
    	"resource_id": resource_id,
    	"force": True,
    	"fields": [{"id": "station", "type": "text"},{"id": "datetime", "type": "timestamp"}, {"id": "PM2_5", "type": "float"}, {"id": "CO", "type": "float"}, {"id": "PM10", "type": "float"}, {"id": "SO2", "type": "float"}, {"id": "O3", "type": "float"}, {"id": "NO2", "type": "float"}],
    	# 'resource': resource,
    	# 'aliases': ['author', 'submitted_on', 'PM2_5', 'CO', 'PM10', 'SO2', 'O3', 'NO2'],
    	# 'records': records
    	# 'primary_key': ['_id'],
    	# 'indexes': ['id'],
	}
	
	request(resource_dict,'datastore_create',api_key)

def url_update(resource_id,api_key):
	# update the url of a resource for the datastore
	resource_dict = {
    	'id': resource_id,
    	'url': 'http://202.121.178.242/datastore/dump/' + resource_id,
    	'revision_id': '1.1'
	}

	request(resource_dict,'resource_update',api_key)

def datastore_upsert(resource_id,data,api_key):
	# insert a new record into the datastore
	resource_dict = {
    	"resource_id": resource_id,
    	"force": True,
    	"records": data,
    	"method": 'insert',
	}

	request(resource_dict,'datastore_upsert',api_key)

def datastore_delete(resource_id,data,api_key):
	# insert a new record into the datastore
	resource_dict = {
    	"resource_id": resource_id,
    	"force": True,
    	"filters": data,
	}

	request(resource_dict,'datastore_delete',api_key)
