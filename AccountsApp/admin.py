from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# from django.utils.translation import gettext_lazy as _
from .models import MyUser


admin.site.register(MyUser)


# custom form class for create and edit
# class MyCustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = MyCustomUser
#         fields = ('email', 'first_name', 'last_name', 'phone_number', 'country',
#                   'city', 'employment_status')  # your custom fields here


# class MyCustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = MyCustomUser
#         fields = UserChangeForm.Meta.fields


# class MyCustomUserAdmin(UserAdmin):
#     form = MyCustomUserChangeForm
#     add_form = MyCustomUserCreationForm
#     model = MyCustomUser
#     list_display = ['email', 'first_name', 'last_name',
#                     'is_staff', 'is_active']  # Adjust according to your needs
#     list_filter = ['is_staff', 'is_active']

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name',
#          'last_name', 'phone_number', 'country', 'city')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff',
#          'is_superuser', 'groups', 'user_permissions')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'country', 'city', 'employment_status', 'is_active', 'is_staff')}
#          ),
#     )
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)


# admin.site.register(MyCustomUser, MyCustomUserAdmin)
