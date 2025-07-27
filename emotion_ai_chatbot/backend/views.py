from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils.emotion_detection import detect_emotion
from .utils.nlp_processing import generate_response
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils.emotion_detection import detect_emotion
from .utils.nlp_processing import generate_response

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
                
            user_message = data.get('message', '')
            
            if not user_message:
                return JsonResponse({'error': 'Message is required'}, status=400)
            
            # Process the message
            emotion = detect_emotion(user_message)
            bot_response = generate_response(user_message, emotion)
            
            return JsonResponse({
                'response': bot_response,
                'emotion': emotion,
                'status': 'success'
            })
            
        except Exception as e:
            return JsonResponse({
                'error': str(e),
                'status': 'error'
            }, status=500)
    
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

def chat_interface(request):
    return render(request, 'chat/index.html')