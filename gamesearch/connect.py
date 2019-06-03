from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import json

es = Elasticsearch('152.136.129.232:9200')

doc = {
    "suggest":{
        "my-suggestion":{
            "text":"Dota",
            "term":{
                "field":"game_name",
                "suggest_mode":"popular"
            }
        }
    }
}
res = es.search(index="wegameindex",doc_type="wegame",body=doc)
res2 = es.search(index="steamindex",doc_type="steam",body=doc)
print(res)
print(res2)

for hit in res['hits']['hits']:
    print(hit['_source']['name'])
    print(hit['_source']['url'])
    print(hit['_source']['price_now'])

doc = {
    "analysis":{
        "filter":{
            "postcode_filter":{
                "type"
            }
        }
    }
}