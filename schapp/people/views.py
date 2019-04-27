from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from people.models import CustomUser
from people.serializers import CustomUserSerializer

@csrf_exempt
def custom_user_list(request):

    if request.method == 'GET':
        custom_user = CustomUser.objects.all()
        serializer = CustomUserSerializer(custom_user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)

@csrf_exempt
def custom_user_detail(request, pk):
    try:
        custom_user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomUserSerializer(custom_user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method =='GET':
        serializer = CustomUserSerializer(custom_user)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        custom_user.delete()
        return HttpResponse(status=204)
