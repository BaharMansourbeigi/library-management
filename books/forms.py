from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "price", "publish_date", "author"]
        widgets = {
            "publish_date": forms.DateInput(attrs={"type": "date"}),
        }
