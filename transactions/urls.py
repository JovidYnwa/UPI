from django.urls import path
from .views import (MerchantCategoryListCreateView,
                    MerchantCategoryRetrieveView,
                    MerchantCategoryUpdateView, 
                    LanguagesView,

                    TestingQueriesDebug,
                    TransactionView, 
                    )

urlpatterns = [
    path('account/', TransactionView.as_view(), name='account'),
    path('language/', LanguagesView.as_view({'get': 'list',
                                             'post': 'create',
                                             'delete':'destroy'}), name='language'),
    path('language/<int:pk>/', LanguagesView.as_view({'get': 'retrieve',
                                                      'delete':'destroy'}), name='language'),

    path('merch-category/', MerchantCategoryListCreateView.as_view(), name='list-category-merchant'),
    path('merch-category/<int:pk>/', MerchantCategoryRetrieveView.as_view(), name='list-category-merchant'),
    path('merch-category/update/<int:pk>/', MerchantCategoryUpdateView.as_view(), name='list-category-merchant'),


    path('debug/', TestingQueriesDebug.as_view()),
]
