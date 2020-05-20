from django.shortcuts import render

# views.py
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })


def message(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer, encoding='utf-8')
    return_str = return_json_str['userRequest']['utterance']

 
    if return_str == 'test':
      return JsonResponse({
        'version': "2.0",
        'template': {
          'outputs': [{
            'simpleText': {
            'text': 'Result: Test Success'
            }
          }],
          'quickReplies': [{
            'label': 'Going back',
            'action': 'message',
            'messageText': 'Going back'
          }]
        }
      })
	

def requestTest(request) :
    str = '테스트입니다'

    return HttpResponse(str)



