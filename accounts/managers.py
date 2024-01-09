from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, first_name, last_name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('User must have a phone number')

        if not email:
            raise ValueError('User must have an email')

        if not first_name or not last_name:
            raise ValueError('User must have both first name and last name')

        email = self.normalize_email(email)
        user = self.model(
            phone_number=phone_number,
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, first_name, last_name, password=None, **extra_fields):
        user = self.create_user(
            phone_number,
            email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user