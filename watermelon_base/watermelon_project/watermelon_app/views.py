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
#    return_str = return_json_str['userRequest']['utterance']

    # if return_str == 'test':
    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [{
                'simpleText': {
                    'text': return_json_str['userRequest']['utterance']
                }
            }]
        }
    })


	

def requestTest(request) :
    

    print(request)



