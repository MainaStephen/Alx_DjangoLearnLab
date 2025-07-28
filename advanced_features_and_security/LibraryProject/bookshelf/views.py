
from django.shortcuts import render, redirect
from .forms import ExampleForm

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('books.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@permission_required('books.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['publication_year']
        Book.objects.create(title=title, author=author, publication_year=year)
        return redirect('book_list')
    return render(request, 'books/book_form.html')

@permission_required('books.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publication_year = request.POST['publication_year']
        book.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'book': book})

@permission_required('books.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')




def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
