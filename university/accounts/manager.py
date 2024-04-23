from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, phone_number=None, **extra_fields):
    
        if not email:
            raise ValueError('The Email must be set')
        if not extra_fields['role']:
            raise ValueError('The role must be set for the user')
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, phone_number=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin') 

        return self.create_user(email, password, phone_number, **extra_fields)
