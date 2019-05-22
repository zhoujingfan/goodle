from django.shortcuts import render
from django.http import JsonResponse
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections

es = Elasticsearch('152.136.129.232:9200')

def search(request):
    print("OK")
    content = {}
    if request.method == "GET":
        keyword = request.GET.get('kw')
        search_type = request.GET.get('search_type')
        # page_num = request.GET.get('page_num')
        if not keyword:
            content['code'] = 104
            content['message'] = "empty keyword"
            return JsonResponse(content)
        if search_type == "game":
            doc = {
                "query": {
                    "match": {
                        "game_name": keyword
                    }
                }
            }
            res = es.search(index="steamindex",doc_type="steam",body=doc)
            result_list = res['hits']['hits']
            content['result_list'] = result_list
        result = "this is result"
        content['code'] = 100
        content['message'] = 'success'
        content['result'] = result
        return JsonResponse(content)
    content = {
        'code': 102,
        'message': 'error!'
    }
    return JsonResponse(content)
def suggest(request):
    content = {}
    return JsonResponse(content)