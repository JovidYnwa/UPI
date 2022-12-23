from django.db import models
from authentification.models import UserAccount

class Transaction(models.Model):
    """Models of customer transactions
    """

    #agent_transaction_id mandatory
    transaction_id = models.CharField(max_length=100,) #Unique, mandatory
    account_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    merchant_id = models.CharField(max_length=15,) #Should relate to the Mercahnts field
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.transaction_id

class Language(models.Model):
    """Models for languages
    """

    lang_id = models.IntegerField(unique=True)
    lang_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.lang_name

class MerchantCategory(models.Model):
    """Merchants category models should be implamented
    """
    pass

class Merchant(models.Model):
    """Merchants model
    """
    
    merch_id = models.CharField(max_length=50,)
    #merchant_category = models.ForeignKey()
    lang_id = models.ForeignKey(Language, to_field='lang_id', on_delete=models.CASCADE)
    merchat_name_ru = models.CharField(max_length=200,)
    merchat_name_eng = models.CharField(max_length=150,)
    merchant_description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    #merchant_logo = 

    def __str__(self) -> str:
        return self.merch_id
