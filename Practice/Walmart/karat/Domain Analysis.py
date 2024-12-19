"""
The "Domain Analysis" problem from Karat assesses your ability to understand and analyze a given problem domain, focusing on identifying key components, relationships, and requirements. This skill is crucial for designing effective software solutions.

Problem Statement:

You are tasked with designing a system for a library management application. The system should handle the following functionalities:

Book Management:
Add new books to the catalog.
Update book information (e.g., title, author, genre).
Remove books from the catalog.
User Management:
Register new users.
Update user information (e.g., contact details).
Deactivate user accounts.
Loan Management:
Allow users to borrow books.
Track due dates and overdue books.
Handle book returns and renewals.
Search Functionality:
Enable users to search for books by title, author, or genre.
Provide recommendations based on user preferences and borrowing history.
Your Task:

Conduct a domain analysis to identify the key entities, their attributes, and the relationships between them. Based on your analysis, design a class diagram that represents the structure of the system. Additionally, outline the main use cases and describe the interactions between users and the system for each functionality.

Considerations:

Think about the data types and constraints for each attribute.
Identify any potential exceptions or error conditions.
Consider scalability and performance requirements.
Ensure that the design supports future extensions, such as adding new functionalities or integrating with other systems.

"""


from typing import List
from datetime import datetime

class Book:
    def __init__(self, id: int, title: str, author: str, genre: str):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.status = "available"
        self.due_date = None

    def update_details(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre

    def borrow(self):
        self.status = "borrowed"

    def return_book(self):
        self.status = "available"
        self.due_date = None

    def renew(self):
        # Extend due date for another week, for example
        self.due_date = datetime.now() + timedelta(days=7)

class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.status = "active"

    def register(self):
        # Register a new user
        pass

    def update_info(self, name: str, email: str):
        self.name = name
        self.email = email

    def deactivate_account(self):
        self.status = "inactive"

    def borrow_book(self, book: Book):
        book.borrow()

    def return_book(self, book: Book):
        book.return_book()

    def renew_book(self, book: Book):
        book.renew()

class Loan:
    def __init__(self, user_id: int, book_id: int, loan_date: datetime, due_date: datetime):
        self.user_id = user_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.due_date = due_date

    def extend_due_date(self):
        self.due_date += timedelta(days=7)

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def search_books(self, query: str):
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]

    def recommend_books(self, user: User):
        # Implement a simple recommendation logic based on past loans
        return self.books  # A placeholder for actual recommendation logic
