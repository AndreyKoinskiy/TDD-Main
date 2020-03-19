from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from .api.serializers import ToDoSerializer
# Create your views here.

@api_view(['GET','DELETE','PUT'])
def get_delete_update_todo(request,pk):
    try:
        print(pk)
        todo = ToDo.objects.get(pk = pk)
    except ToDo.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    # get details of a single todo
    if request.method == 'GET':
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)
    # delete a single todo
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    # update details of a single todo
    elif request.method == 'PUT':
        serializer = ToDoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    return Response({})

@api_view(['GET','POST'])
def get_post_todos(request):
    #get all puppies
    if request.method == 'GET':
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many = True)
        return Response(serializer.data)
    #insert a new record for a puppy
    elif request.method == 'POST':
        data = {
            'text':request.data.get('text'),
            'status':request.data.get('status'),
            'user':request.data.get('user'),
            'created_at':request.data.get('created_at')
        }
        serializer = ToDoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)