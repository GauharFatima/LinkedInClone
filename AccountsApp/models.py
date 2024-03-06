from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.contrib.auth.models import BaseUserManager
# from django.core.exceptions import ValidationError
# from django_countries.fields import CountryField


class MyUser(models.Model):
    EMPLOYMENT_STATUS = [('employed', 'Employed'), ('student', 'Student')]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15, blank=True, null=True)
    password = models.CharField(max_length=50)
    # country = CountryField(
    #     blank_label='(select country)', null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    employment_status = models.CharField(
        max_length=10, choices=EMPLOYMENT_STATUS, null=True)


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, first_name, last_name, password=None,  phone_number=None, country=None, city=None, employment_status=None, **extra_fields): # noqa
#         """
#         Create and return a regular user with an email, first name, last name, and other details. # noqa
#         """
#         if not email:
#             raise ValueError(
#                 'Users must have an email address to login/sign-in')

#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#             phone_number=phone_number,
#             country=country,
#             city=city,
#             employment_status=employment_status,
#             **extra_fields
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, first_name, last_name, password, **extra_fields): # noqa
#         """
#         Create and return a superuser with required information.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if not all([extra_fields.get('is_staff'), extra_fields.get('is_superuser')]): # noqa
#             raise ValueError(
#                 'Superuser must have is_staff=True and is_superuser=True.')

#         return self.create_user(email, first_name, last_name, password, **extra_fields) # noqa


# class MyCustomUser(AbstractBaseUser, PermissionsMixin):
#     EMPLOYMENT_STATUS = [('employed', 'Employed'), ('student', 'Student')]
#     employment_status = models.CharField(
#         max_length=10, choices=EMPLOYMENT_STATUS,  blank=True, null=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(
#         max_length=15, blank=True, null=True)
#     country = CountryField(
#         blank_label='(select country)', blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = MyUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name',
#                        'country', 'city', 'employment_status']

#     def __str__(self):
#         return self.email
