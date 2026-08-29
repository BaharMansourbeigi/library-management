from django import forms
from django.core.validators import MinValueValidator

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "price", "publish_date", "author"]
        widgets = {
            "publish_date": forms.DateInput(attrs={"type": "date"}),
        }


class SearchForm(forms.Form):
    s = forms.CharField(
        required=False,
        label="Search",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )


class FilterForm(forms.Form):
    min_price = forms.DecimalField(
        required=False,
        validators=[MinValueValidator(0)],
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    max_price = forms.DecimalField(
        required=False,
        validators=[MinValueValidator(0)],
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    from_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
            }
        ),
    )
    to_date = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
            }
        ),
    )
