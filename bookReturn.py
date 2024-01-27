from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pandas as pd
from datetime import date, datetime
import database as d





def return_book(book_return_Id):
    """
    This function is for returning the checked out books,
    and keeping a log of the return data  in Loan reservation
    table .

    If a reserved book is returned then a message is shown to
    inform the member who reserved the book that it is 
    available to be issued.

    Parameters: 
    book_return_Id:book_return_Id is used to get the Book Id 
    from the Librarian

    """
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    if book_return_Id.isdigit():
        conn,cur = d.db_connection()
        cur.execute("Select status from BOOKLIST where Book_Id=?",(book_return_Id,))
        value = cur.fetchall()
        result = value[0][0]
        print(result)
        if result == 'Available':
            messagebox.showinfo("Information","This Book already exists")
        elif result == 'Not Available':
            cur.execute("UPDATE BOOKLIST SET Status='Available' WHERE Book_Id=?",(book_return_Id,))
            conn.commit()
            cur.execute("SELECT * from LOAN_RESERVATION where Book_Info_Id=? and Return_Date IS NULL",(book_return_Id,))
            value1 = cur.fetchall()
            print(value1)
                     
            if value1[0][3] == None :
                        query = "UPDATE LOAN_RESERVATION SET Return_Date=? where Book_Info_Id=? and Return_Date IS NULL"
                        cur.execute(query,(current_date,book_return_Id))
                        conn.commit()
                        messagebox.showinfo("Information","Book returned successfully!")
        else:
            cur.execute("UPDATE BOOKLIST SET Status='Available' WHERE Book_Id=?",(book_return_Id,))
            conn.commit()
            cur.execute("SELECT * from LOAN_RESERVATION where Book_Info_Id=? and Return_Date IS NULL",(book_return_Id,))
            value1 = cur.fetchall()
            print(value)
            if value1[0][3] == None:
                query = "UPDATE LOAN_RESERVATION SET Return_Date=? where Book_Info_Id=? and Return_Date IS NULL"
                cur.execute(query,(current_date,book_return_Id))
                conn.commit()
                messagebox.showinfo("Information","Notify the Member who reserved the book that the book is now available to be issued!")
    else:
        messagebox.showerror("showerror","Please enter a valid Book Id")

print(return_book.__doc__)



