from django.contrib.auth import get_user_model
from django.forms import forms, ModelForm, CharField
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class UserUpdateForm(ModelForm):
    validate_numeric = RegexValidator(regex='^[0-9]*$', message='Use only digits')
    age = CharField(max_length=2, required=True, validators=[validate_numeric])
    age.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'age']

    def clean_email(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.email
        else:
            return self.cleaned_data['email']

    def clean_age(self):
        new_age = self.cleaned_data['age']
        if int(new_age) < 18:
            raise ValidationError('You must be 18 or older')
        return new_age


