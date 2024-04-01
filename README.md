### Library Management System Project README

## Overview
This Library Management System project, that offers comprehensive functionalities for efficient library management. With six modules, two text files, and a detailed README file, this project streamlines various library tasks.

## Modules Description

### 1. Database Files
- **book_list.txt**: Contains book details such as Book ID, Author, Genre, Purchase Date, and Purchase Price.
- **loan_reservation.txt**: Stores loan and reservation data including Book ID, Checkout Date, Return Date, Reservation Date, and Member ID.
- **SQLite Database**: Data from text files is imported into 'library.db' for database management.

### 2. bookSearch.py
- Enables librarians to search for books in the Booklist database.
- Allows users to search for books by title, displaying results in a tree view format.
- Provides an option to reset the search and retrieve the entire list of books.

### 3. bookCheckout.py
- Facilitates book checkout processes for library members.
- Records checkout transactions, capturing checkout dates, member IDs, and book IDs.
- Allows book reservations if unavailable, with notifications sent upon book return.

### 4. bookReturn.py
- Manages book return processes, updating transaction logs and book statuses accordingly.
- Sends notifications to members upon the return of reserved books, making them available for checkout.

### 5. bookSelect.py
- Offers budget-based book recommendations.
- Presents graphs illustrating popular genres and book titles based on checkout and reservation data.
- Provides functionality to recommend books within the library's budget range.

### 6. menu.py
- Serves as the main graphical user interface (GUI) for librarians.
- Integrates all modules into a seamless user experience, facilitating library management tasks.

### 7. database.py
- Manages database connections and table creation within SQLite.
- Initializes data from text files into database tables for system operations.
- Updates tables dynamically during system interactions, ensuring accurate record-keeping.

## Usage
- **Running the System**: Execute `menu.py` to launch the GUI and access all functionalities.
- **Database Configuration**: Ensure proper database connectivity and initialization before using the system.
- **Input Validation**: Follow provided test cases to validate input data and system responses.
- **Graph Visualization**: Note that graph labels may not be fully visible due to long titles; zooming may be required for better visibility.

## Contributing
- Contributions and improvements are welcome.
- Fork the repository, make changes, and submit pull requests for review.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Special thanks to all contributors and supporters of this project.
- Inspired by the need for efficient library management systems in educational and organizational settings.

