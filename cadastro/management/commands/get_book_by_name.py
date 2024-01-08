# get_book_by_name
from django.core.management.base import BaseCommand
from cadastro.models import Livro

class Command(BaseCommand):
    help = "Get books from the database based on its name"

    def add_arguments(self, parser):
        parser.add_argument(
            'book_name',
            help='get book by its name'
        )

    def handle(self, *args, **options):
        book_title_parameter = options.get('book_name', None)

        if book_title_parameter is not None:
            books = Livro.objects.filter(titulo__icontains=book_title_parameter)
            message = f"List of books with the name '{book_title_parameter}':"
        else:
            books = Livro.objects.all()
            message = "List of all books:"

        if books:
            self.stdout.write(message)
            for book in books:
                self.stdout.write(f"- {book}")
        else:
            self.stdout.write("No books found in the database.")
