from django.shortcuts import render, redirect

from .forms import BookForm
from .models import Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)


def addbooks(request):
    if request.method == 'POST':
        form = BookForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    books = Book.objects.all()
    context = {
        'books': books,
        'form': form
    }
    return render(request, 'books_add.html', context)


def viewbooks(request, id):
    books = Book.objects.filter(id=id)
    context = {
        'books': books
    }
    return render(request, 'books_id.html', context)
