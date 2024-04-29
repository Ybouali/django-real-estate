from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError(_('Invalid email address'))
        
    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        if not username:
            raise ValidationError(_('You must provide a username'))
        if not first_name:
            raise ValidationError(_('You must provide a firstname'))
        if not last_name:
            raise ValidationError(_('You must provide a lastname'))
        if not email:
            raise ValidationError(_('You must provide a email'))
        else:
            email = self.normalize_email(email)
            self.email_validator(email)
        if not password:
            raise ValidationError(_('You must provide a password'))
        
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser most have is_staff = True'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser most have is_superuser = True'))
        
        if not password:
            raise ValidationError(_('Superuser must have a password'))
        
        if not email:
            raise ValidationError(_('Superuser must have an email'))
        else:
            email = self.normalize_email(email)
            self.email_validator(email)
        
        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)

        return user