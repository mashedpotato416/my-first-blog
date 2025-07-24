from django.urls import path
from . import views
### In Development this is needed
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
###

# Pages in the blog app
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
### In Development this is needed
urlpatterns += staticfiles_urlpatterns()
###