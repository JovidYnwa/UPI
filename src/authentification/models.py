from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, 
                                        PermissionsMixin, 
                                        BaseUserManager
                                    )


class UserAccountManager(BaseUserManager):
    """This call need only becase we overwrite User model
    """

    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError("User shold provide phone number")

        user = self.model(phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None):
        if not phone:
            raise ValueError("User shold provide phone number")
        
        user = self.model(phone=phone, is_staff=True, is_active=True, is_superuser=True)
        user.set_password(password)
        user.save()
        return user


class UpiUser(AbstractBaseUser, PermissionsMixin):
    """This is main User model
    """

    phone = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "phone"
    # REQUIRED_FIELDS = ["phone"]

    def get_full_name(self):
        return self.phone

    def get_short_name(self):
        return self.phone

    def __str__(self):
        return self.phone


class UserAccount(models.Model):
    """User accounts models
    """
    
    phone_id = models.ForeignKey(UpiUser, to_field='phone', on_delete=models.CASCADE)
    account = models.CharField(max_length=20,)
    #clnt_id  #In case if will need unique id from our customers
    bank_id = models.CharField(max_length=200,)
    account_type = models.CharField(max_length=10, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.phone_id)
