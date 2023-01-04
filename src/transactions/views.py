import datetime
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.permissions import (IsAuthenticated, 
                                        IsAdminUser,                                        
                                        IsAuthenticatedOrReadOnly,                                        
                                        )

from transactions.serializer import (MerchantCategorySerializer, 
                                     TransactionSerializer, 
                                     LanguageSerializer,
                                     )
from transactions.models import (Transaction, 
                                 Language,
                                 MerchantCategory
                                 )



class TransactionView(APIView):
    """View for getting all customers accounts
    """

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass


class LanguagesView(viewsets.ModelViewSet):
    """Viewset for Language model
    Overwriting permission function for delete action
    """

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def get_permissions(self):        
        if self.action in ['delete', 'create']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]


class MerchantCategoryListCreateView(generics.ListCreateAPIView):
    """Generics views
    Create only for admin user
    List only from authenticated
    """

    queryset = MerchantCategory.objects.filter(end_date__gt=datetime.datetime.now())
    serializer_class = MerchantCategorySerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]


class MerchantCategoryRetrieveView(generics.RetrieveAPIView):
    """Generics views for Deitail view
    Create only for admin user
    List only from authenticated
    """

    permission_classes = [IsAuthenticated,]
    queryset = MerchantCategory.objects.filter(end_date__gt=datetime.datetime.now())
    serializer_class = MerchantCategorySerializer
    lookup_field = 'pk'

class MerchantCategoryUpdateView(generics.UpdateAPIView):
    """Generics views for Update view
    """
    
    permission_classes = [IsAdminUser,]
    queryset = MerchantCategory.objects.filter(end_date__gt=datetime.datetime.now())
    serializer_class = MerchantCategorySerializer
    lookup_field = 'pk'
