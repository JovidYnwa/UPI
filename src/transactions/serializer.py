from transactions.models import (Transaction, 
                                 Language,
                                 MerchantCategory)
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class MerchantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MerchantCategory
        fields = '__all__'