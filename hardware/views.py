from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def send_to_hardware(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            value = data.get('value')
            
            # Simulate sending the value to hardware
            # Example: send_value_to_hardware(value)
            
            return JsonResponse({'status': 'success', 'value_sent': value}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)
