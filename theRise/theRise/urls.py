from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('', include('dairy.urls', namespace='dairy')),
    path('users/', include('users.urls', namespace='users')),
]
