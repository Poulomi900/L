 
This is a project on Library Management System created by Student Id (F220504). In this project there are 6 modules , 2 txt files and 1 Readme file.

Module description:

1 : Database Files 

    Here there are 2 database files in txt format as :

    a)book_list.txt -> This stores BOOk Id,Author,Genre,Purchase Date,Purchase Price
    b)loan_reservation.txt -> This stores Book Id , Checkout data, Return Data, Reservation Data , Member Id

    We will be reading data from these 2 txt files and storing them in our SQLite Database called 'library.db'


2: bookSearch.py

   This module is used by the Librarian to search book from the Booklist database.

   Testcase 1 :
    
    Type the name of the book you want to search that is present in the booklist database 
    (please check what books are available in the database before typing using the scrollbar present in the leftside)

    Search : Dune
    (Click on Search button) --> you can see  books along with their id,genre,title,Status in the treeview
    (click on Reset button) --> To get back the entire list of books 



3.bookCheckout.py

  This function is used to checkout books and keep a record of the checkout date,member id and book id as well as 
  reservation date if opted.

  If a book of a particular Book Id is not available then another of the same Title can be checked out if the member
  wants.

  If all the books of the same title are not available , member will have the option to reserve the book
  and the Librarian will have the option to notify the member once the book is returned.

  If the member Id or book Id is not valid then an error message will be shown.




   Eg: Testcase 1 : Do validity check :
                   a)Enter a 5 digit or string member Id --> You will get a error message stating "Invalid member Id"

       Testcase 2 : (to issue a particular book with a unique if it if available)

                    Member Id: 1123
                    Book Id : 2
                    Book issued successfully! (inside information messagebox) 
                    Book Id,Member Id ,checkout Date gets inserted in loan_reservation database
                    Status gets updated in Booklist database

       Testcase 3: (to check if a book of particular Id is not available but another book of same title is available, 
                  then to give the member the option to issue it)

                  Member Id: 1120
                  Book Id : 1
                  Book issued successfully!

                  Member Id:1121
                  Book Id: 1
                  A different book with this Title is available , do you want to take it ? (inside askyesno messagebox)

                 a) Yes 
                   Book issued successfully!
                   Book Id,Member Id ,checkout Date gets inserted in loan_reservation database
                   Status gets updated in Booklist database
                 b) No
                   (messagebox disappears) 

        Testcase 4 : (to reserve a book if all the copies of the book is not available)
                   
                  Member Id: 1120
                  Book Id : 1
                  This Book is currently not available , do you want to reserve the book ? 

                  a) Yes
                    Book reserved successfully!
                    Book Id,Member Id ,Reservation Date gets inserted in loan_reservation database
                    Status gets updated in Booklist database

                 b) No
                   (messagebox disappears) 

        Testcase 5 : (if the book has only 1 copy and it is already issued then an option to reserve the book will come, 
                     but if a member wants that book a second time then it will show a message that the 'book is already reserved' )
                  
                  Member Id: 1128
                  Book Id : 8
                  Book issued successfully!

                  Member Id: 1129
                  Book Id : 8
                  This Book is currently not available , do you want to reserve the book ? 

                  a) Yes
                    Book reserved successfully!
                    Book Id,Member Id ,Reservation Date gets inserted in loan_reservation database
                    Status gets updated in Booklist database

                 b) No
                   (messagebox disappears) 

                  Member Id: 1123
                  Book Id : 8
                  This Book is already reserved!




4.bookReturn.py

  This function is for returning the checked out books,and keeping a log of the return data  in Loan reservation table .
  
  If a reserved book is returned then a message is shown to inform the member who reserved the book that it is available to be issued.



  Example testcases : 
             
             Testcase 1 : Do a validity check to see if the bookid is a digit 

             Book Id : hjsf5
             Please enter a valid Book Id

             Testcase 2 : Trying to Return a book using Book Id , if the book is already Available

             Book Id : 4
             This Book already exists!

             Testcase 3 : Returning a book using Book Id which is 'Issued'

             Book Id : 48
             Book returned successfully!
             Book Id and return date gets updated in loan_reservation database
             Status gets updated in Booklist database

             Testcase 4 : Returning a book which is not available as well as is reseved after that
             by some another member

             Book Id : 8

             Book returned successfully!
             Book Id and return date gets updated in loan_reservation database
             Status gets updated in Booklist database
             Notify the Member who reserved the book that the book is now available to be issued!(inside information messagebox)




5. bookSelect.py
            Note : A budget of 1000£ is set as the Library's budget and the entered budget should be above 10£

            Example testcases:

            Testcase 1 : 
                      Enter your budget:800
                      Click on "Recommend Genre" button -->(A graph consisting of Most popular genre will be displayed based on Checkout and 
                                                           Reserve data which is calculated by number of times the Book id appears in the loan_reservation table
                                                           and joining it with BOOKLIST table)
                                                           
                      Click on "Recommend book by Title" button -->(A graph consisting of Most popular Books will be displayed based on Checkout and 
                                                           Reserve data which is calculated by number of times the Book id appears in the loan_reservation table)

            Testcase 2 : 
                     Enter your budget:1001
                     Click on  "Recommend Genre" button --> Please enter a budget amount above 10£ within Library's budget range (inside messagebox)
                     Click on "Recommend book by Title" button --> Please enter a budget amount above 10£ within Library's budget range (inside messagebox)

            Testcase 3:
                    Enter your budget:0
                    Click on  "Recommend Genre" button --> Please enter a budget amount above 10£ within Library's budget range
                    Click on "Recommend book by Title" button --> Please enter a budget amount above 10£ within Library's budget range

          Please note , the label in the x axis is not visible for the graphs as the title and genre names are long.Kindly zoom the graphs 
          after opening.
          
          A list of book titles and book genre are printed based on the popularity on the terminal on click of the two buttons along with the graphs.


6. menu.py
           
          Inside this python file , i have the entire code for Graphical user Interface , which the Librarian will be using.
          It is the main python program from where we are calling all the other modules.



7. database.py 
          
           This python file contains the database connection function which all the other modules uses to interact with the database.
           It also has the function that creates table in the sqlite database and does the initialization of data in the database.

           Inside the database there are two tables :
           1) BOOKLIST  --> Here i am storing the book information from book_list.txt
           2) LOAN_Reservation  --> Here i am storing the checkout,return,reservation date , book id, member id from loan_reservation.txt

          These tables are updated when different functionalities are occuring inside the different functions.We are also fetching data
          as and when needed inside the functions.

                                   



             

        


                  


                  

                                    

