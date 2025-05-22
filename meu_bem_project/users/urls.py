from django.urls import path
from .views import CreateUserView, api_root

urlpatterns = [
    path('', api_root),
    path('users/', CreateUserView.as_view(), name='create_user'),
]
