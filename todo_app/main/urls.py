from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.addTask, name='add-task'),  # add a new task
    path('task-complete/<int:pk>', views.taskComplete,
         name='taskComplete'),    # mark a task as complete
    path('unmark-task/<int:pk>', views.unmarkTask,
         name='unmarkTask'),  # mark a task as in-complete
    path('edit-task/<int:pk>', views.editTask,
         name='editTask'),    # edit a task
    path('delete-task/<int:pk>', views.deleteTask,
         name='deleteTask'),  # delete a task
]
