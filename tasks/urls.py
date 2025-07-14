from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('list/', views.TaskListView.as_view(), name='list'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('<int:pk>/detail/', views.TaskDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete')
]
