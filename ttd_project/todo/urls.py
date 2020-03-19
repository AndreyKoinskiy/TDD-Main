from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/todos/<pk>',views.get_delete_update_todo,name = 'get_delete_update_todo'),
    path('api/v1/todos/',views.get_post_todos, name = 'get_post_todos'),
]