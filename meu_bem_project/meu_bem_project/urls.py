from django.contrib import admin
from django.urls import path, include  # <-- CERTIFIQUE-SE QUE 'include' ESTÁ IMPORTADO

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # <-- ISSO CONECTA O ENDPOINT /api/users/
]
