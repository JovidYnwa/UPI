from django.urls import path
from .views import CreateAccountView

urlpatterns = [
    path('account/', CreateAccountView.as_view(), name=''),
]