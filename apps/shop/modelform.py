from django import forms
from django.core.exceptions import ValidationError

from content.utils.md5 import md5
from .models import CustomerLogin


class AddToCartForm(forms.ModelForm):
    product_amount = forms.IntegerField(min_value=1, initial=1)


