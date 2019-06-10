from django.shortcuts import render
from django.http import JsonResponse
from elasticsearch import Elasticsearch
from elasticsearch_dsl.connections import connections

es = Elasticsearch('152.136.129.232:9200')

def search(request):
    content = {}
    if request.method == "POST":
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
                },
                # "match": {
                #     "game_summary":keyword
                # }
            },
            "highlight": {
                "fields":{
                    "game_name":{}
                }
            }
        }
        baseweb = request.POST.get('baseWeb')
        print(baseweb)
        print(len(baseweb))
        print(keyword)  
        res = es.search(index="steamindex",doc_type="steam",body=doc)
        res2 = es.search(index='wegameindex',doc_type='wegame',body=doc)
        result_list2 = res2['hits']['hits']
        result_list1 = res['hits']['hits']
        station = []
        if len(result_list1)>0:
            station.append('steam')
        if len(result_list2)>0:
            station.append('wegame')
        if len(baseweb)>6:
            total = res['hits']['total']+res2['hits']['total']
            result_list  = result_list1
            for item in result_list2:
                result_list.append(item)
        elif baseweb=="steam":
            total = res['hits']['total']
            result_list = result_list1
        elif baseweb=='uplay':
            total = res2['hits']['total']
            result_list = result_list2
        else:
            content['code']=102
            content['message']="参数错误"
            return JsonResponse(content)
        print(result_list1)
        print(result_list2)
        print(len(result_list1))
        print(len(result_list2))
        # for num in range(page_num*10,min(len(result_list), page_num*10+10)):
        #     result.append(result_list[num])
        # content['result'] = result
        content['result_list'] = result_list
        # content['result_list2'] = result_list2
        content['total']=total
        content['station'] = station
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