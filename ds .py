# --------------------------------------------
# Data Structures Assignment 2
# Library Book Management System
# Using Single Linked List and Stack
# --------------------------------------------

# Node class for Book record
class BookNode:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None

# Linked List class for managing books
class BookList:
    def __init__(self):
        self.head = None

    def insertBook(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        if self.head is None:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print(f" Book '{title}' added successfully.")

    def deleteBook(self, book_id):
        temp = self.head
        prev = None
        while temp:
            if temp.book_id == book_id:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f" Book '{temp.title}' deleted successfully.")
                return
            prev = temp
            temp = temp.next
        print(" Book not found.")

    def searchBook(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                print(f"📘 Book Found -> ID: {temp.book_id}, Title: {temp.title}, Author: {temp.author}, Status: {temp.status}")
                return temp
            temp = temp.next
        print(" Book not found.")
        return None

    def displayBooks(self):
        temp = self.head
        if not temp:
            print(" No books in the library.")
            return
        print("\n Current Books in Library:")
        while temp:
            print(f"  ID: {temp.book_id}, Title: {temp.title}, Author: {temp.author}, Status: {temp.status}")
            temp = temp.next
        print("--------------------------------------------")


# Stack for managing transactions (Undo functionality)
class TransactionStack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("No transactions to undo.")
            return None

    def isEmpty(self):
        return len(self.stack) == 0

    def viewTransactions(self):
        if self.isEmpty():
            print(" No recent transactions.")
            return
        print("\n Recent Transactions:")
        for action in
