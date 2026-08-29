from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm, FilterForm, SearchForm
from .models import Book


def get_filter_books(request):
    books = Book.objects.all()
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        s = search_form.cleaned_data.get("s")
        if s:
            books = Book.objects.filter(
                Q(title__icontains=s)
                | Q(author__first_name__icontains=s)
                | Q(author__last_name__icontains=s)
            )
    filter_form = FilterForm(request.GET)
    if filter_form.is_valid():
        min_price = filter_form.cleaned_data.get("min_price")
        max_price = filter_form.cleaned_data.get("max_price")
        from_date = filter_form.cleaned_data.get("from_date")
        to_date = filter_form.cleaned_data.get("to_date")

        if min_price is not None:
            books = books.filter(price__gte=min_price)
        if max_price is not None:
            books = books.filter(price__lte=max_price)
        if from_date:
            books = books.filter(publish_date__gte=from_date)
        if to_date:
            books = books.filter(publish_date__lte=to_date)

    return books, search_form, filter_form


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "book_form.html", {"form": form})


def book_list(request):
    books, search_form, filter_form = get_filter_books(request)

    return render(
        request,
        "book_list.html",
        {"books": books, "search_form": search_form, "filter_form": filter_form},
    )


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_detail.html", {"book": book})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "book_form.html", {"form": form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "book_confirm_delete.html", {"book": book})


def book_delete_filtered(request):
    books, _, _ = get_filter_books(request)
    if request.method == "POST":
        books.delete()
        return redirect("book_list")
    return render(request, "book_confirm_delete_filtered.html", {"books": books})
