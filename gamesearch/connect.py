from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import json

es = Elasticsearch('152.136.129.232:9200')

doc = {
    "query": {
        "match": {
            "name": "孤岛惊魂"
        }
    }
}

res = es.search(index="wegameindex",doc_type="wegame",body=doc)

for hit in res['hits']['hits']:
    print(hit['_source']['name'])
    print(hit['_source']['url'])
    print(hit['_source']['price_now'])
