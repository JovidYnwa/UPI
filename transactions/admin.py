from django.contrib import admin
from .models import (Transaction, 
                     Language,
                     MerchantCategory,
                     Merchant
                    )

admin.site.register(Transaction,)
admin.site.register(Language,)

admin.site.register(MerchantCategory)
admin.site.register(Merchant)