from django.urls import path

from dairy.views import index

app_name = 'dairy'

urlpatterns = [
    path('', index, name='index'),
]