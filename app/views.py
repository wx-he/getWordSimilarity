from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import spacy
# Create your views here.
@csrf_exempt
def getsimilarity(request,word1,word2):
    nlp=spacy.load('en_core_web_md')
    word1=nlp(word1)
    word2=nlp(word2)
    s=word1.similarity(word2)
    response={}
    response['similarity']=s
    return JsonResponse(response)

@csrf_exempt
def getsimilaritypost(request):
    if request.method != 'POST':
        return HttpResponse(status=404)

    json_data = json.loads(request.body)
    word1 = json_data['word1']
    word2 = json_data['word2']
    nlp=spacy.load('en_core_web_md')
    word1=nlp(word1)
    word2=nlp(word2)
    response={}
    response['similarity']=word1.similarity(word2)
    return JsonResponse(response)
