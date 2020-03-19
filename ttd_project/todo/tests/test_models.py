from django.test import TestCase
import datetime
from django.contrib.auth.models import User

from ..models import ToDo


class ToDoTest(TestCase):
    """ Test module for ToDo model """

    def setUp(self):
        
        user = User.objects.create_user(username='TestUser')

        ToDo.objects.create(text='First TODO 1', status=False,
                            user=user)
        ToDo.objects.create(text='Second TODO 1', status=False,
                            user=user)
        ToDo.objects.create(text='Third TODO 1', status=False,
                            user=user)

    def test_text_representation(self):
        
        user = User.objects.get(username='TestUser')
      
        fpick = ToDo.objects.get(text = 'First TODO 1')
        spick = ToDo.objects.get(text = 'Second TODO 1')

        self.assertEqual(str(fpick),f'False | First TODO 1 ==>{user.username}')
        self.assertEqual(str(spick),f'False | Second TODO 1 ==>{user.username}')