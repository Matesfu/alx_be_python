class Book:
    def __init__(self, title, author, is_checked_out = False):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out
    def checking_out(self):
        self._is_checked_out = True
    def get_check_out_value(self):
        return self._is_checked_out
    def unchecking(self):
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.checking_out()
    def list_available_books(self):
        for book in self._books:
            if book.get_check_out_value() == False:
                print(f"{book.title} by {book.author}")
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.unchecking()