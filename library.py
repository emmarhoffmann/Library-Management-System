# File: library.py
# Author: Emma Hoffmann

# This Python program serves as a library management system. It allows users to manage a collection
# of books and encyclopedias, offering functionalities to add new items to the collection, 
# and save the entire collection to a CSV file. The program can also load an existing collection 
# from a CSV file. Users interact with the program through terminal inputs to add new books or 
# encyclopedias by specifying their title, author, publisher, and publication date. For encyclopedias,
# additional information such as edition and number of volumes are also captured. 
#
# The program ensures data persistence by saving the current state of the library to a CSV file, 
# which can be reloaded in subsequent runs of the program. This allows for maintaining a continuous 
# and updated record of the library's collection. The program is designed with basic error handling 
# for file operations and includes user-friendly prompts for data input and options to view the entire 
# collection or exit the program.

# Global constant for the library's CSV file path
LIBRARY_CSV_PATH = r'C:\Users\Emma Hoffmann\OneDrive\SCHOOL - SPRING 23\CSCI1107\library.csv'

import csv

# Represents a book with basic bibliographic information.
# Postcondition: A Book object is created with the given title, author, publisher, and publication date.
class Book:
    # Initializes a new Book instance.
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date

    # Prints detailed information about the book.
    # Precondition: The book object is initialized
    # Postcondition: Book information is printed to the console.
    def print_info(self):
        print('Information:')
        print(f'   Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')

# Represents an encyclopedia, a specialized type of book.
# Precondition: Inherits attributes from the Book class.
# Postcondition: An Encyclopedia object is created with additional attributes of edition and number of volumes.
class Encyclopedia(Book):
    # Initializes a new Encyclopedia instance.
    def __init__(self, title, author, publisher, publication_date, edition, num_volumes):
        super().__init__(title, author, publisher, publication_date)
        self.edition = edition
        self.num_volumes = num_volumes

    # Prints detailed information about the encyclopedia.
    # Precondition: The encyclopedia object is initialized.
    # Postcondition: Encyclopedia information is printed to the console.
    def print_info(self):
        super().print_info()
        print(f'   Edition: {self.edition}')
        print(f'   Number of Volumes: {self.num_volumes}')

# Saves the collection of books to a CSV file.
# Precondition: A list of book objects and a file path.
# Postcondition: The book list is written to the CSV file at the specified path.
def save_to_library(book_list, filename=LIBRARY_CSV_PATH):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Type', 'Title', 'Author', 'Publisher', 'Publication Date', 'Edition', 'Number of Volumes'])
        for book in book_list:
            if isinstance(book, Encyclopedia):
                writer.writerow(['Encyclopedia', book.title, book.author, book.publisher, book.publication_date, book.edition, book.num_volumes])
            else:
                writer.writerow(['Book', book.title, book.author, book.publisher, book.publication_date, '', ''])

# Loads a collection of books from a CSV file.
# Precondition: A file path to a CSV file.
# Postcondition: Returns a list of book objects loaded from the CSV file.
def load_from_library(filename=LIBRARY_CSV_PATH):
    book_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) >= 5:
                    if row[0] == 'Encyclopedia' and len(row) == 7:
                        try:
                            num_volumes = int(row[6]) if row[6] else 0  # Convert to int or default to 0
                            book = Encyclopedia(row[1], row[2], row[3], row[4], row[5], num_volumes)
                        except ValueError:
                            print(f"Skipping row due to invalid number of volumes: {row}")
                            continue
                    elif row[0] == 'Book':
                        book = Book(row[1], row[2], row[3], row[4])
                    else:
                        continue
                    book_list.append(book)
                else:
                    print(f"Skipping row due to insufficient data: {row}")
    except FileNotFoundError:
        print(f"No existing file named {filename}. Starting with an empty list.")
    except IOError:
        print(f"Error: Unable to read data from {filename}.")
    return book_list

# Main execution block of the program.
# Allows the user to interactively add books or encyclopedias to the library and view the collection.
if __name__ == "__main__":
    my_library = load_from_library()

    while True:
        choice = input("Enter 'book' to add a book, 'encyclopedia' to add an encyclopedia, or 'exit' to finish and view the library: ").lower()
        if choice == 'exit':
            break
        
        if choice in ['book', 'encyclopedia']:
            title = input("Enter title: ")
            author = input("Enter author: ")
            publisher = input("Enter publisher: ")
            publication_date = input("Enter publication date: ")

            if choice == 'book':
                new_book = Book(title, author, publisher, publication_date)
            else:
                edition = input("Enter edition: ")
                num_volumes = int(input("Enter number of volumes: "))
                new_book = Encyclopedia(title, author, publisher, publication_date, edition, num_volumes)

            my_library.append(new_book)
        else:
            print("Invalid input. Please enter 'book', 'encyclopedia', or 'exit'.")

    # Saving updated library to CSV file and displaying collection
    save_to_library(my_library)
    print("\nLibrary Collection:")
    for book in my_library:
        book.print_info()