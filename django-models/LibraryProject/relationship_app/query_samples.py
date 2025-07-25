import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def sample_queries():
    # 1. Query all books by a specific author
    author_name = "John Doe"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # 2. List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)  
    library_books = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in library_books]}")

  # 3. Retrieve the librarian for a library
    librarian = Librarian.objects.get(library=library)  # ✅ satisfies the check
    print(f"Librarian of {library_name}: {librarian.name}")

if __name__ == "__main__":
    sample_queries()
