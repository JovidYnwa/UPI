from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from authentification.serializer import (UserAccountSerializer,
                                        UserDataSerializer)


class CreateAccountView(APIView):
    """View for creating account for UpiUser
    """
    
    def post(self, request):
        
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UserDataView(APIView):
    """View for user data info
    """
    
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


#celery beat for customer birthday