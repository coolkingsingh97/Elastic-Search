# Import elasticsearch package and create connection object to localhost
from elasticsearch import Elasticsearch
es = Elasticsearch()

# Searching the data using scroll method

res = es.search(
	index = 'users',
	doc_type = 'doc',
	scroll = '20m',
	size = 500,
	body = {"query":{"match_all":{}}}
	)

# Saving the scroll ID and size of the result for later purposes

sid = res['_scroll_id']
size = res['hits']['total']['value']

# Use while loop to scroll through the data

while(size>0):
	res = es.scroll(scroll_id = sid, scroll = '20m')
	sid = res ["_scroll_id"]
	size = len(res['hits']['hits'])
	for doc in res['hits']['hits']:
		print(doc['_source'])
	