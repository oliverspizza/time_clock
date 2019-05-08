from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from people.models import CustomUser
from people.serializers import CustomUserSerializer

@api_view(['GET','POST'])
def custom_user_list(request, format=None):

    if request.method == 'GET':
        custom_user = CustomUser.objects.all()
        serializer = CustomUserSerializer(custom_user, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def custom_user_detail(request, pk, format=None):
    try:
        custom_user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CustomUserSerializer(custom_user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method =='GET':
        serializer = CustomUserSerializer(custom_user)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        custom_user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
