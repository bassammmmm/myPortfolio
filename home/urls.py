from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('project-details/<int:id>', views.project_details, name = 'project_details')
]