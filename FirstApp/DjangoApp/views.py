from django.http import HttpResponse
import json

def Index(request):
    
	data={'Message':'Hello World!'}
	return HttpResponse(json.dumps(data), content_type='application/json')

# Create your views here.
