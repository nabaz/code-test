from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Difference
from api.serializers.difference_serializers import DifferenceSerializer

@csrf_exempt
def difference(request):

    if request.method == 'GET' and not request.GET.get('number'):
        differences = Difference.objects.all()
        serializer = DifferenceSerializer(differences, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'GET' and request.GET.get('number'):
        number_query =  request.GET.get('number');
        differences = Difference.objects.filter(number = number_query)
        serializer = DifferenceSerializer(differences, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DifferenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
