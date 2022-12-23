from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from authentification.models import UpiUser

from authentification.serializer import UserAccountSerializer


class CreateAccountView(APIView):
    """View for creating account for UpiUser
    """
    
    def post(self, request):

        request_phone = request.data["phone_id"]
        user_exists = UpiUser.objects.filter(phone=request_phone).count()
        if user_exists == 0:
            new_user = UpiUser(phone=request_phone)
            new_user.save()

        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)