from django import forms
# from django.core.exceptions import ValidationError

from .models import Account

#admin registration
class AdminAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['user_name',
                  'password',
                  'full_name',
                  'email',
                  'auth_type']
    def clean_password(self):
        password = self.cleaned_data.get('password')
        user_name = self.cleaned_data.get('user_name')
        if password == user_name :
            raise forms.ValidationError('password must not be the same with user_name')
        print(user_name)
        return password

#Registration for user
class UserAccountForm(AdminAccountForm):
    class Meta:
        model =  Account
        fields = ['user_name',
                  'password',
                  'email']
