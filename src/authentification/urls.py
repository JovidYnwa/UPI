from django.urls import path
from .views import CreateAccountView, UserDataView

urlpatterns = [
    path('account/', CreateAccountView.as_view(), name=''),
    path('account-data/', UserDataView.as_view(), name=''),
]