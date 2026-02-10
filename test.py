import pytest
from LibrarySystem import Book

def test_initialize_library():
    book = Book("Clean Code", "Robert Cecil Martin")
    assert book.title == "Clean Code"
    assert book.author == "Robert Cecil Martin"
    assert book.available is True

def test_borrow_when_available():
    book1 = Book("1984", "George Orwell")
    available = book1.borrow()
    assert available is True
    assert book1.available is False

def test_borrow_when_not_available():
    book2 = Book("The Hobbit", "J.R.R. Tolkien")
    book2.borrow()
    available = book2.borrow()
    assert available is False
    assert book2.available is False

def test_return_book():
    book = Book("Brave New World", "Aldous Huxley")
    book.borrow()
    book.return_book()
    assert book.available is True