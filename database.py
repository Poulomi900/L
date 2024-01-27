from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pandas as pd
from datetime import date, datetime
import matplotlib.pyplot as plt




def db_connection():

        """
        
        This function is used to create and 
        connect to Library.db database ,
        this is the common function which 
        is used by all the modules to interact with the database
        
        """

        conn = sqlite3.connect('library.db')
        cur = conn.cursor()
        return conn,cur


#Tables are created 

def table_creation():

        """
        This function is used to create tables,
        read data from the book_list.txt and 
        loan_reservation.txt files and initialize
        the same in the two tables BOOKLIST and 
        LOAN_Reservation

         """


        conn,cur = db_connection()
        book_table = cur.execute("""CREATE TABLE IF NOT EXISTS BOOKLIST (
        Book_Id INTEGER PRIMARY KEY NOT NULL,
        Genre TEXT NOT NULL,
        Title TEXT NOT NULL,
        Purchase_Price INTEGER NOT NULL,
        Purchase_Date TEXT NOT NULL,
        status TEXT  NOT NULL
        )""")

        


        loan_reservation_table = cur.execute("""CREATE TABLE IF NOT EXISTS LOAN_Reservation (
        Book_Info_Id INTEGER NOT NULL,
        Reservation_Date TEXT NOT NULL,
        Checkout_Date TEXT NOT NULL,
        Return_Date TEXT NOT NULL,
        Member_ID INTEGER NOT NULL
        )""")


        cur.execute("""Select * from BOOKLIST""")
        book_val = cur.fetchall()
        conn.commit()
        cur.execute("""Select * from LOAN_Reservation""")
        loan_val = cur.fetchall()
        conn.commit()

         

        

        df1 = pd.read_csv("book_list.txt",sep=",",header=None,names=["Book_Id","Genre","Title","Author","Purchase_Price","Purchase_Date"])
        df2 = pd.read_csv("loan_reservation.txt",sep=",",header=None,names=["Book_Info_Id","Reservation_Date","Checkout_Date","Return_Date","Member_ID"])

       
        if len(book_val) == 0 and len(loan_val) == 0:
                
                df1.to_sql('BOOKLIST', conn, if_exists='replace', index = False)
                df2.to_sql('LOAN_Reservation', conn, if_exists='replace', index = False)
                alter_book = cur.execute("""ALTER TABLE BOOKLIST ADD status TEXT DEFAULT 'Available'""" )
                conn.commit()

        

        

        conn.commit()
        conn.close()


print(db_connection.__doc__)
print(table_creation.__doc__)





