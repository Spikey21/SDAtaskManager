from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('tasks/',views.tasks, name = 'tasks'),
    path('tasks/<int:taskId>/delete/',views.delete_task, name = 'delete_task'),
    path('create/',views.create, name = 'create'),
    path('tasks/<int:taskId>/detail/',views.detail, name = 'detail'),
    path('tasks/<int:taskId>/complete/',views.complete_task, name = 'complete_task'),
]