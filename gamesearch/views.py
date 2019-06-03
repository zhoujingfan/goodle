from django.shortcuts import render
from django.http import JsonResponse
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections

es = Elasticsearch('152.136.129.232:9200')

def search(request):
    print("OK")
    content = {}
    if request.method == "POST":
        print("POST")
        keyword = request.POST.get('keyword')
        # search_type = request.POST.get('search_type')
        # page_num = int(request.POST.get('page_num'))
        # print(page_num)
        if not keyword:
            content['code'] = 104
            content['message'] = "empty keyword"
            return JsonResponse(content)
        
        doc = {

            "query": {
                "match": {
                    "game_name": keyword
                }
            }
        }
        res = es.search(index="steamindex",doc_type="steam",body=doc)
        res2 = es.search(index='wegameindex',doc_type='wegame',body=doc)
        total = res['hits']['total']+res2['hits']['total']
        result_list2 = res2['hits']['hits']
        result_list = res['hits']['hits']
        print(len(result_list2))
        print(len(result_list))
        result = []
        for item in result_list2:
            result_list.append(item)
        print(len(result_list))
        # for num in range(page_num*10,min(len(result_list), page_num*10+10)):
        #     result.append(result_list[num])
        # content['result'] = result
        content['result_list'] = result_list
        # content['result_list2'] = result_list2
        content['total']=total
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

def fuzzy_search(request):
    content = {}
    if request.method == "GET":
        keyword = request.GTE.get('keyWord')
        if not keyword:
            content['code'] = 104
            content['message'] = 'empty keyword'
            return JsonResponse(content)
        doc = {
            "query":{
                "match":{
                    "query":"game_name",
                    "fields":keyword,
                    "fuzziness":"AUTO"
                }
            }
        }
        res = es.search(index="steamindex",doc_type="steam",body=doc)
        result_list = res['hits']['hits']
        content['result_list'] = result_list
        result = "thsi is result"
        content['code'] = 100
        content['message'] = 'success'
        content['result'] = result
        return JsonResponse(content)

def suggest(request):
    content = {}
    print("ok")
    if request.method  == "POST":
        keyword = request.POST.get('keyword')
        if not keyword:
            content['code'] = 104
            content['message'] = 'empty keyword'
            return JsonResponse(content)
        doc = {
            "suggest":{
                "my-suggestion":{
                    "prefix":keyword,
                    "term":{
                        "field":"game_name",
                        "suggest_mode":"popular"
                    }
                }
            }
        }
        res_steam = es.search(index="steamindex",doc_type="steam",body=doc)
        res_wegame = es.search(index="wegameindex",doc_type="wegame",body=doc)
        result_steam = res_steam['suggest']['my-suggestion'][0]['options']
        result_wegame = res_wegame['suggest']['my-suggestion'][0]['options']
        res = []
        for re in result_steam:
            
            res.append({'value':re['text']})
        for re in result_wegame:
            res.append({'value':re['text']})
        content['code'] = 100
        content['res'] = res
    return JsonResponse(content)