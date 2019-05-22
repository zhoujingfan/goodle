from django.db import models
from elasticsearch_dsl import DocType,Date,Nested,Boolean,analyzer,Completion,Keyword,Text,Integer,Float
from elasticsearch_dsl.connections import connections

class SteamType(DocType):
    game_name = Text(analyzer="ik_max_word")
    release_date = Date()
    game_price = Keyword()
    game_summary = Text(analyzer="ik_max_word")
    game_img = Keyword()
    review_list = Text(analyzer="ik_max_word")
    price_discount = Text(analyzer="ik_max_word")
    game_url = Keyword()

    class Meta:
        index = "steamindex"
        dot_type = "steam"

class WegameType(DocType):
    url = Keyword()
    name = Text(analyzer="ik_max_word")
    price_now = Text(analyzer="ik_max_word")
    price_old = Text(analyzer="ik_max_word")

    class Meta:
        index = "wegameindex"
        doc_type = "wegame"
