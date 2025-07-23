from django.urls import path
from . import views

# Pages in the blog app
urlpatterns = [
    path('', views.post_list, name='post_list'),
]