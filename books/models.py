from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    publish_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        to="Author", on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self):

        return f"{self.title}"

    class Meta:
        ordering = ["-created_at"]


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):

        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):

        return f"{self.name}"
