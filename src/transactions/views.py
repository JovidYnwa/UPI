from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated, 
                                        IsAdminUser,
                                        IsAuthenticatedOrReadOnly,
                                        )
from rest_framework.decorators import permission_classes, api_view

from transactions.serializer import (TransactionSerializer, 
                                     LanguageSerializer,
                                     )
from transactions.models import (Transaction, 
                                 Language,
                                 )



class TransactionView(APIView):
    """View for getting all customers accounts
    """

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        queryset = Transaction.objects.all()
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)


class LanguagesView(viewsets.ModelViewSet):
    """Viewst for Language model
    Overwriting permission function for delete action
    """

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def get_permissions(self):
        
        if self.action in ['delete']:
            permission_classes = [IsAdminUser]
        permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
