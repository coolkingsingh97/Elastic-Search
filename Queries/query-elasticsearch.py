from elasticsearch import Elasticsearch
es = Elasticsearch()

# Creating JSON object to send as a query to Elasticsearch

doc = {"query":{"match_all":{}}}

# Passing the object to Elasticsearch using search method

res = es.search(index="users",body=doc,size=10)

# Printing the documents returned
# print(res['hits']['hits'])
# OR

for doc in res['hits']['hits']:
	print(doc['_source'])

