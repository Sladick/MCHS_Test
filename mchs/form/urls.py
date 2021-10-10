from django.urls import path
from .views import Post


urlpatterns = [
    path('', Post.as_view())
]