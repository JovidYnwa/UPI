from django.urls import path
from .views import (TransactionView, 
                    LanguagesView,
                    )

urlpatterns = [
    path('account/', TransactionView.as_view(), name='account'),
    path('language/', LanguagesView.as_view({'get': 'list',
                                             'post': 'create',
                                             'delete':'destroy'}), name='language'),
    path('language/<int:pk>/', LanguagesView.as_view({'get': 'retrieve',
                                                      'delete':'destroy'}), name='language'),
]
