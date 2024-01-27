from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3
import pandas as pd
from datetime import date, datetime
import matplotlib.pyplot as plt
from bookSearch import SearchBook
import database as d
from bookCheckout import checkout
from bookReturn import return_book
from bookSelect import setup_recommendation,fetch_book_data,get_recommendations,recommend_books






class MainClass:

   


    def __init__(self,root):

        """
        This function contains all the GUI elements 
        and functions which are used to call the 
        functions from seprate python files.


        """

        self.root = root
        self.root.geometry("1000x700")
        self.root.title("Library Management System")
        self.root.config(bg="pink")
        self.notebook = ttk.Notebook(self.root) # creating tabs in the window
        Frame1 = ttk.Frame(self.notebook,width=500,height=400) 
        Frame2 = ttk.Frame(self.notebook,width=500,height=400)
        Frame3 = ttk.Frame(self.notebook,width=500,height=400)
        Frame4 = ttk.Frame(self.notebook,width=500,height=400)
 
        label1 = ttk.Label(Frame1, text = "Search Book")
        label2 = ttk.Label(Frame2, text = "Checkout Book")
        label3 = ttk.Label(Frame3, text = "Return Book")
        label4 = ttk.Label(Frame4, text = "Recommend Book")

        label1.pack(pady = 60, padx = 80)
        label2.pack(pady = 60, padx = 80)
        label3.pack(pady = 60, padx = 80)
        label4.pack(pady = 60, padx = 80)
         
        Frame1.pack(fill= tk.BOTH, expand=True)
        Frame2.pack(fill= tk.BOTH, expand=True)
        Frame3.pack(fill= tk.BOTH, expand=True)
        Frame4.pack(fill= tk.BOTH, expand=True)
 
        self.notebook.add(Frame1, text = "Book Search")
        self.notebook.add(Frame2, text = "CheckOut Book")
        self.notebook.add(Frame3, text = "Return Book")
        self.notebook.add(Frame4, text = "Recommend Book")

        self.notebook.pack(padx = 40, pady = 60, expand = True, fill = tk.BOTH)




        # Fetching the entire book details from the BOOKLIST Table

        conn,cur = d.db_connection()
        query = "Select * from BOOKLIST"
        cur.execute(query)
        rows=cur.fetchall()
       

         
        # Creating a vertical scrollbar , to scroll through the list of 50 books

        vertical_sc_bar = ttk.Scrollbar(Frame1,orient ="vertical")
        vertical_sc_bar.pack(side ='left', fill ='y')
        my_treeview = ttk.Treeview(Frame1,height=8,selectmode="extended",yscrollcommand=vertical_sc_bar.set)
        vertical_sc_bar.config(command=my_treeview.yview)

        
        my_treeview['columns'] = ('book_id','genre','title','author','status')
        my_treeview['show'] = 'headings'
        my_treeview.column("#0",width=0) # Setting the default column width of treeview to 0,to stop it from displaying
        my_treeview.column("book_id",width=60,stretch=YES)
        my_treeview.column("genre",width=100,stretch=YES)
        my_treeview.column("title",width=180,stretch=YES)
        my_treeview.column("author",width=100,stretch=YES)
        my_treeview.column("status",width=60,stretch=YES)


        my_treeview.heading(0,text="book_id")
        my_treeview.heading(1,text="genre")
        my_treeview.heading(2,text="title")
        my_treeview.heading(3,text="author")
        my_treeview.heading(4,text="status")

        my_treeview.pack()

        # Inserting the values from BOOKLIST database which is stored in 'rows' to the treeview, only the columns that we want to view by indexing

        for row in rows:
            my_treeview.insert("", 'end',  values=(row[0], row[1], row[2], row[3], row[6]))

    


        def update(rows):

            """
            Clear the treeview and insert the values of rows which is fetched above 
            on click.
            
            This function is called in both SearchBook and clear functions which
            has on click events.

            """
            my_treeview.delete(*my_treeview.get_children())
            for val in rows:
                my_treeview.insert('','end',values=(val[0], val[1], val[2], val[3], val[6]))




        def calling_searchbook():

            """
            This function is used to call the SearchBook 
            function from bookSearch.py

            """
            rows = SearchBook(bookname.get())
            update(rows)



        def clear():    

            """
            This function is used to get back the entire list of books 
            by clicking on reset button.

            """                 
            rows = SearchBook("")
            update(rows)

        


        def calling_checkout():
            """
            This function is used to call checkout 
            function from bookCheckout.py
            
            """

            rows = checkout(enter_memberId.get(),enter_bookId.get())

        
        
        def calling_return_book():
            """
            This function is used to call return_book 
            function from bookReturn.py

            """
            rows = return_book(return_bookId.get())


    





        
            
       

        search_label = Label(Frame1,text="Search")
        search_label.pack(side=tk.LEFT,padx=10,anchor=CENTER)
        search_entry = Entry(Frame1,textvariable=bookname)
        search_entry.pack(side=tk.LEFT,padx=6,anchor=CENTER)
        button = Button(Frame1,text="Search",command=calling_searchbook)
        button.pack(side=tk.LEFT,padx=6,anchor=CENTER)
        button = Button(Frame1,text="Reset",command=clear)
        button.pack(side=tk.LEFT,padx=6,anchor=CENTER)


        member_Id = Label(Frame2,text="Member Id")
        member_Id.pack(side=tk.TOP,padx=10,anchor=CENTER)
        member_Id = Entry(Frame2,textvariable=enter_memberId)
        member_Id.pack(side=tk.TOP,padx=10,anchor=CENTER)

        bookId_label = Label(Frame2,text="Book Id")
        bookId_label.pack(side=tk.TOP,padx=10,anchor=CENTER)
        bookId = Entry(Frame2,textvariable=enter_bookId)
        bookId.pack(side=tk.TOP,padx=10,anchor=CENTER)


        checkout_update = Button(Frame2,text="CheckOut",command=calling_checkout)
        checkout_update.pack(side=tk.TOP,padx=10,anchor=CENTER)


 

        bookId_label = Label(Frame3,text="Book Id")
        bookId_label.pack(side=tk.TOP,padx=10,anchor=CENTER)
        bookId = Entry(Frame3,textvariable=return_bookId)
        bookId.pack(side=tk.TOP,padx=10,anchor=CENTER)

        return_update = Button(Frame3,text="Return Book",command=calling_return_book)
        return_update.pack(side=tk.TOP,padx=10,anchor=CENTER)


        Fixed_Budget_amt = Label(Frame4,text="Library's fixed budget : 1000£")
        Fixed_Budget_amt.pack(side=tk.TOP,padx=10,anchor=CENTER)


        self.budget_amt = IntVar()
        Budget_amt = Label(Frame4,text="Enter budget amount above 10£")
        Budget_amt.pack(side=tk.TOP,padx=10,anchor=CENTER)
        Budget_amt = Entry(Frame4,textvariable=self.budget_amt)
        Budget_amt.pack(side=tk.TOP,padx=10,anchor=CENTER)

        genre_recommendation = Button(Frame4,text="Recommended Genre ",command=self.get_recommended_books_gui)
        genre_recommendation.pack(side=tk.TOP,padx=10,anchor=CENTER)

        self.title_recommendation = StringVar()
        title_label = Label(Frame4, text="Enter Book Title for Recommendation")
        title_label.pack(side=tk.TOP, padx=10, anchor=CENTER)
        title_entry = Entry(Frame4, textvariable=self.title_recommendation)
        title_entry.pack(side=tk.TOP, padx=10, anchor=CENTER)
        title_button = Button(Frame4, text="Recommend by Title", command=self.get_title_recommendations_gui)
        title_button.pack(side=tk.TOP, padx=10, anchor=CENTER)

        
        #genre_recommendation = Button(Frame4,text="Recommended Book by Title ",command=calling_book_recommend)
        #genre_recommendation.pack(side=tk.TOP,padx=10,anchor=CENTER)

    def get_recommended_books_gui(self):
        budget = self.budget_amt.get()
        recommend_books(budget)

    def get_title_recommendations_gui(self):
        title = self.title_recommendation.get()
        recommended_titles = get_recommendations(title)
        if recommended_titles.empty:
            messagebox.showinfo("Recommendations", "No recommendations found.")
        else:
            recommendations = "\n".join(recommended_titles)
            messagebox.showinfo("Recommendations", f"Recommended books for '{title}':\n{recommendations}")


        
        
        

        

d.table_creation() # Calling the table_creation function from database.py


root = Tk() # Tk() is used to create a new window in python
enter_memberId= StringVar() 
enter_bookId=StringVar()
return_bookId=StringVar()
budget_amt = IntVar()
bookname = StringVar()


if __name__ == '__main__':
        obj = MainClass(root)
        root.mainloop() 





