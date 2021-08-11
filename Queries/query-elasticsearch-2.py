from elasticsearch import Elasticsearch
from pandas.io.json import json_normalize

es = Elasticsearch()

# Creating JSON object to send as a query to Elasticsearch

doc = {"query":{"match_all":{}}}

# Passing the object to Elasticsearch using search method

res = es.search(index="users",body=doc,size=10)

# Converting JSON result into a dataframe

df =json_normalize(res['hits']['hits'])

# Other types of queries

# doc={"query":{"match":{"name":"Ronald Goodman"}}}
# res=es.search(index="users",body=doc,size=10)
# print(res['hits']['hits'][0]['_source'])

# Using Lucene Syntax

# res = es.search(index="users",q="name:Ronald Goodman",size=10)
# print(res['hits']['hits'][0]['_source'])

# Get City Jamesberg
# doc= {"query":{"match":{"city":"Jamesberg"}}}

# res = es.search(index="users",body=doc,size=10)

# print(res['hits']['hits'])

# Using boolean in queries 
# 1. must
# 2. must not
# 3. should


doc = {"query":{"bool":{"must":{"match":{"city":"Jamesberg"}},"filter":{"term":{"zip":"74444"}}}}}

res = es.search(index="users",body=doc,size=10)

print(res['hits']['hits'])



