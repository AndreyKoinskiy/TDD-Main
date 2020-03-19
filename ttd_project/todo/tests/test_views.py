from django.test import TestCase, Client
import json
from rest_framework import status
from django.urls import reverse
from ..models import ToDo
from ..api.serializers import ToDoSerializer
from django.contrib.auth.models import User
# inititalize the APIClient app
client = Client()

class GetAllToDosTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='TestUser')

        ToDo.objects.create(text='Mikle TODO', status=False,
                            user=user)
        ToDo.objects.create(text='Sara TODO 1', status=False,
                            user=user)
        ToDo.objects.create(text='Ruslan TODO 1', status=False,
                            user=user)
        ToDo.objects.create(text='Mikola TODO 1', status=False,
                            user=user)

    def test_get_all_todos(self):
        # get API response
        response = client.get(reverse('get_post_todos'))
        # get data from db
        todos = ToDo.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleToDoTest(TestCase):
    """ Test module for GET single ToDo API """

    def setUp(self):
        user = User.objects.create_user(username='TestUser')

        self.first = ToDo.objects.create(text='First TODO 1', status=False,
                            user=user)
        self.second = ToDo.objects.create(text='Second TODO 1', status=False,
                            user=user)
        self.third = ToDo.objects.create(text='Third TODO 1', status=False,
                            user=user)

    def test_get_valid_single_todo(self):
        response = client.get(reverse('get_delete_update_todo',kwargs={'pk':self.first.pk}))
        todo = ToDo.objects.get(pk=self.first.pk)
        serializer = ToDoSerializer(todo)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
def test_get_invalid_single_todo(self):
    response = client.get(reverse('get_delete_update_todo',kwargs={'pk':30}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewToDoTest(TestCase):
    """ Test molule for inserting a new todo """

    def setUp(self):
        user = User.objects.create_user(username='TestUser')

        self.valid_payload = {
            'text':'test Text',
            'status':'False',
            'user':user.pk,
            'created_at':'2020-03-19 21:44:14.736657'
        }

        self.invalid_payload = {
            'text':'',
            'status':'False',
            'user':user.pk,
            'created_at':''
        }
    def test_create_valid_todo(self):
        response = client.post(
            reverse('get_post_todos'),
            data = json.dumps(self.valid_payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_todo(self):
        response = client.post(
            reverse('get_post_todos'),
            data = json.dumps(self.invalid_payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleToDoTest(TestCase):
    """ Test module for updating an existing todo record """

    def setUp(self):

        user = User.objects.create_user(username='TestUser')

        self.first = ToDo.objects.create(text='First TODO 1', status=False,
                            user=user)
        self.second = ToDo.objects.create(text='Second TODO 1', status=False,
                            user=user)
        
        self.valid_payload = {
            'text':'First TODO 1',
            'status':'False',
            'user':user.pk,
        }

        self.invalid_payload = {
            'text':'First TODO 22',
            'status':'False',
            'user':'44',
        }

    def test_valid_update_todo(self):
        response = client.put(
            reverse('get_delete_update_todo', kwargs = {'pk':self.first.pk}),
            data=json.dumps(self.valid_payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_todo(self):
        response = client.put(
            reverse('get_delete_update_todo', kwargs = {'pk':self.first.pk}),
            data = json.dumps(self.invalid_payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleToDoTest(TestCase):
    """ Test module for deleting an existing todo record """

    def setUp(self):
        
        user = User.objects.create_user(username='TestUser')

        self.first = ToDo.objects.create(text='First TODO 1', status=False,
                            user=user)
        self.second = ToDo.objects.create(text='Second TODO 1', status=False,
                            user=user)
    
    def test_valid_delete_todo(self):
        response = client.delete(
            reverse('get_delete_update_todo', kwargs={'pk':self.first.pk}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_invalid_delete_todo(self):
        response = client.delete(
            reverse('get_delete_update_todo', kwargs = {'pk':30})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    