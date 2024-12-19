"""
The "Book Endings" problem from Karat involves designing a system to manage a collection of books, focusing on efficiently adding, removing, and retrieving books based on their titles. The problem typically requires implementing data structures that support these operations with optimal time and space complexities.

Problem Statement:

You are tasked with creating a class BookCollection that supports the following operations:

Add a Book: Add a book to the collection. If the book already exists, update its information.
Remove a Book: Remove a book from the collection. If the book does not exist, return an error.
Retrieve a Book: Retrieve the information of a book by its title. If the book does not exist, return an error

"""

#Approach:
#To implement this system efficiently, 
# consider using a hash table (dictionary in Python) 
# to store book titles as keys and their corresponding 
# information as values. This approach ensures that 
# each operation—addition, removal, and retrieval—can 
# be performed in average constant time, O(1).


class BookCollection:
    def __init__(self):
        self.books = {}

    def add_book(self, title, info):
        self.books[title] = info

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
        else:
            raise ValueError(f"Book '{title}' not found in the collection.")

    def retrieve_book(self, title):
        if title in self.books:
            return self.books[title]
        else:
            raise ValueError(f"Book '{title}' not found in the collection.")
#Time Complexity: Each operation (add, remove, retrieve) 
# has an average time complexity of O(1) due to the use of a 
# hash table.

#Space Complexity: The space complexity is O(n), where n is the
#  number of books in the collection, as we store each book's 
# title and information.