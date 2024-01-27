from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pandas as pd
from datetime import date, datetime
import database as d



def checkout(member_Id,bookId):
    
    """
    The function to checkout books and 
    keep a record of the checkout date,
    member id and book id as well as 
    reservation date if opted.

    Parameters : 
    member_Id : It is used to get member Id as input from Librarian

    bookId :It is used to get book Id as user input from Librarian
    
    """
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y")
    if len(member_Id)==4 and member_Id.isdigit() and bookId.isdigit() and bookId is not '0':
                conn,cur = d.db_connection()
                cur.execute("Select status,title from BOOKLIST where Book_Id=?",(bookId,))
                value = cur.fetchall()
                result1 =  value[0][0] # fetching the status of book of a specific id and storing here
                result2 = value[0][1] # fetching the Book name of a specific id and storing here
                #print(value)
                if result1 == 'Not Available': #If book of a specific id is not available check for book of same name

                    q = "Select Book_Id,title,status from BOOKLIST where title=? and status='Available'"
                    cur.execute(q,(result2,))
                    val = cur.fetchone() 
                    res3 = 'Not Available' #Initialising a default value to res3
                    print(result1)
                    
                    if val is not None :
                        res1 = val[0] # storing the book Id that is fetched and stored in q by indexing
                        res2 = val[1] # storing the Book name that is fetched and stored in q by indexing
                        res3 = val[2] # storing the status that is fetched and stored in q by indexing

                        if res3 == 'Available':

                            if messagebox.askyesno("askyesno","A different book with this Title is available , do you want to take it ?"):

                                q = "UPDATE BOOKLIST SET Status='Not Available' WHERE Book_Id=?"
                                cur.execute(q,(res1,))
                                conn.commit()
                                cur.execute("INSERT INTO LOAN_RESERVATION(Book_Info_Id,Checkout_Date,Member_ID) VALUES ("+res1+",'"+current_date+"','"+member_Id+"')")
                                conn.commit()
                                messagebox.showinfo("Information","Book Issued successfully!")
                        

                    else:
                            if messagebox.askyesno("askyesno","Book is currently not available , do you want to reserve the book ?"):

                                cur.execute("UPDATE BOOKLIST SET Status='Reserved' WHERE Book_Id=?",(bookId,))
                                conn.commit()
                                cur.execute("INSERT INTO LOAN_RESERVATION(Book_Info_Id,Reservation_date,Member_ID) VALUES ("+bookId+",'"+current_date+"','"+member_Id+"')")
                                conn.commit()
                                messagebox.showinfo("Information","Book reserved successfully!")
                    
                elif result1 == 'Available':
                            q = "UPDATE BOOKLIST SET Status='Not Available' WHERE Book_Id=?"
                            cur.execute(q,(bookId,))
                            conn.commit()
                            cur.execute("INSERT INTO LOAN_RESERVATION(Book_Info_Id,Checkout_Date,Member_ID) VALUES ("+bookId+",'"+current_date+"','"+member_Id+"')")
                            conn.commit()
                            messagebox.showinfo("Information","Book Issued successfully!")
                            
                else: 
                    messagebox.showinfo("Information","Book is already reserved")
    else:
        messagebox.showerror("showerror","You have entered a invalid member Id or Book Id") 


print(checkout.__doc__)



                    
    


