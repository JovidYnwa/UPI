from authentification.models import (UserAccount,
                                    UserData,)
from rest_framework import serializers


class UserAccountSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = UserAccount
        fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = UserData
        fields = '__all__'