from django.core.management.base import BaseCommand
from cadastro.models import Livro

class Command(BaseCommand):
    help = "Get all books from the database"

    def handle(self, *args, **options):
        books = Livro.objects.filter(id__gt=1)

        if books:
            self.stdout.write("List of all books:")
            for book in books:
                self.stdout.write(f"- {book}")
        else:
            self.stdout.write("No books found in the database.")
