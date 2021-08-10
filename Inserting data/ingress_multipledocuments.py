# Importing required libraries
from elasticsearch import Elasticsearch
from faker import Faker
# To insert multiple documents at a time
from elasticsearch import helpers


# Creating faker object
fake = Faker()

# If our connection is running on localhost
es = Elasticsearch()

# Creating an array of JSON Objects

actions =[{
	"_index":"users",
	"_type": "doc",
	"_source": {
		"name": fake.name(),
		"street" : fake.street_address(),
		"city": fake.city(),
		"zip":fake.zipcode()
	}
}
for x in range(998)
	]

# Passing the array of JSON to elasticsearch using the helper function
res = helpers.bulk(es, actions)


# Confirmation how many lines added
print(res[0])


