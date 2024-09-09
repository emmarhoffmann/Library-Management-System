# Library Management System

## About
This Python-based Library Management System allows users to manage a collection of books and encyclopedias. The program enables users to add new items to the collection, save the collection to a CSV file, and load an existing collection from the file. Users interact with the program through terminal inputs, and the system supports persistent data storage for ongoing usage.

## Features
- **Add New Items**: Allows users to add books or encyclopedias to the collection, with specific fields for title, author, publisher, and publication date.
- **Data Persistence**: The library's collection is saved to a CSV file, which can be reloaded in subsequent program executions.
- **Encyclopedia Support**: In addition to books, the system manages encyclopedias with extra fields such as edition and number of volumes.
- **Error Handling**: Includes basic error handling for file operations and ensures a smooth user experience.

## Project Structure
- `library.py`: The main script that handles user input, book and encyclopedia creation, and data management. It supports loading from and saving to the CSV file.
- `library.csv`: Stores the library's collection of books and encyclopedias in a structured format.
