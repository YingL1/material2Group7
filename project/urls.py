from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
    url(r'^register/', views.register, name='register')
]