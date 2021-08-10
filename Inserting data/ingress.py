# Importing required libraries
from elasticsearch import Elasticsearch
from faker import Faker
# To insert multiple documents at a time
from elasticsearch import helpers


# Creating faker object
fake = Faker()

# If our connection is running on localhost
es = Elasticsearch()

# We can also mention the IP address if required
# es = Elasticsearch({'127.0.0.1'})

# Using index method to send data

## First let's create the JSON object used in the body of our method

doc = {"name": fake.name(),"street" : fake.street_address(), "city": fake.city(), "zip":fake.zipcode()}

# Calling Index method

res = es.index(index = "users", doc_type="doc",body=doc)

# Confirmation if the document has been added
print(res['result'])


