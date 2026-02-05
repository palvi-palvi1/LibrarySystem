import pytest
from LibrarySystem import Book

def test_book_borrow_success():
    book = Book("Clean Code", "Robert Cecil Martin")
    success = book.borrow()
    assert success is True
    assert book.available is False

def test_initialize_library():
    book = Book("Clean Code", "Robert Cecil Martin")
    assert book.title == "Clean Code"
    assert book.author == "Robert Cecil Martin"
    assert book.available is True

def test_borrow_when_available(self):
     book1 = Book("Data Analysis", "Dr. Anil Maheshwari")
     available = book1.borrow()
     self.assertTrue(available is True)
     self.assertFalse(book1.available)

def test_borrow_when_not_available(self):
     book2 = Book("Project Managment", "Harold Kerzner")
     book2.borrow()
     available = book2.borrow()
     self.assertFalse(available is False)
     self.assertFalse(book2.available)

def test_return_book(self):
    book = Book("Python", "Eric Matthes")
    book.borrow()
    book.return_book()
    self.assertTrue(book.available)