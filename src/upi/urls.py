from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authen/', include('authentification.urls')),
    path('tran/', include('transactions.urls')),

    #djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
