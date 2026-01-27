import pytest
from LibrarySystem import Library
from LibrarySystem import Book
def test_book_borrow_success():
    book = Book("Clean Code", "Robert Cecil Martin")
    success = book.borrow()
    assert success is True
    assert book.available is False

def test_borrow_book_available():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    result = lib.borrow_book("Dune")
    assert result == True
    assert lib.books[0].available == False