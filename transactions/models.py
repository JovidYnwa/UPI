from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from authentification.models import UserAccount

from base.services import (get_path_upload_merchant, 
                        validate_size_image)


class Language(models.Model):
    """Model for languages
    """

    lang_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.lang_name


class MerchantCategory(models.Model):
    """Merchants category models should be implamented
    """

    lang_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100,)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateTimeField(default=timezone.datetime(2999, 12, 12, tzinfo=timezone.utc))
    category_logo = models.ImageField(        
        upload_to=get_path_upload_merchant,
        validators=[FileExtensionValidator(allowed_extensions=['jpg',]),
        validate_size_image], 
        blank=True,
        null=True
    )

    def __str__(self):
        return self.category_name


class Merchant(models.Model):
    """Merchants model
    """
    
    merch_id = models.CharField(max_length=50, blank=True, null=True) #comes from vendor side
    merch_cat_id = models.ForeignKey(MerchantCategory, on_delete=models.CASCADE)
    lang_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    merchat_name = models.CharField(max_length=200,)
    merchant_description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateTimeField(default=timezone.datetime(2999, 12, 1))
    merchant_logo = models.ImageField(        
        upload_to=get_path_upload_merchant,
        validators=[FileExtensionValidator(allowed_extensions=['jpg',]),
        validate_size_image], 
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return self.merch_id


class Transaction(models.Model):
    """Models of customer transactions
    """

    partner_transaction_id = models.CharField(max_length=100, blank=True, null=True) #Comes from bank side
    account_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE) 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.transaction_id


class BankLogos(models.Model):
    """under development
    """
    pass
