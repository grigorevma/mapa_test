from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False,
                                 help_text='Optional.')
        
    last_name = forms.CharField(max_length=30, required=False,
                                help_text='Optional.')

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            if field.label is None:
                field.widget.attrs.update({'placeholder': field_name.upper(), "size": 40})
            else:
                field.widget.attrs.update({'placeholder': field.label, "size": 40})


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

