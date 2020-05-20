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

@csrf_exempt
def message(request):

    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == 'test':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "test ok"
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                }]
            }
        })


def requestTest(request) :
    str = '테스트입니다'

    return HttpResponse(str)



