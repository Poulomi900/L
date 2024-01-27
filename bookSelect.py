from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, datetime
import database as d
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


cosine_sim = None

# Set up the recommendation system
def setup_recommendation():
    global cosine_sim
    books = fetch_book_data()
    books['Genre'] = books['Genre'].fillna('')
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(books['Genre'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return books



# Fetch book data from the database
def fetch_book_data():
    conn, cur = d.db_connection()
    query = """SELECT Book_Id, Title, Genre FROM BOOKLIST"""
    cur.execute(query)
    data = cur.fetchall()
    columns = ['Book_Id', 'Title', 'Genre']
    return pd.DataFrame(data, columns=columns)

# Get book recommendations based on a title
def get_recommendations(title):
    if cosine_sim is None:  # Check if cosine_sim has been set up
        print("Recommendation system is not set up.")
        return []

    books = fetch_book_data()  # Fetch current book data

    if title not in books['Title'].values:
        print(f"No recommendations found for the title: {title}")
        return []

    idx = books.index[books['Title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    book_indices = [i[0] for i in sim_scores]
    return books['Title'].iloc[book_indices]



# Initialize the recommendation system outside functions
books_data = setup_recommendation()





# function to recommend popular books based on checkout count
def recommend_books(budget):
    conn, cur = d.db_connection()
    library_budget = 1000
    if budget >= 10 and budget <= library_budget:
        query = cur.execute("""Select count(LOAN_Reservation.Book_Info_Id),(BOOKLIST.Title) FROM BOOKLIST  
                                    Join LOAN_Reservation  on BOOKLIST.Book_Id = LOAN_Reservation.Book_Info_Id 
                                    group by BOOKLIST.Title order by count(LOAN_Reservation.Book_Info_Id) DESC """)
        val = cur.fetchall()
        df = pd.DataFrame(val, columns=['Count of checkout by BookId', 'Title'])
        df.plot(kind='bar', x='Title', y='Count of checkout by BookId')
        plt.xlabel("Popularity of Books by Title")
        plt.ylabel("Count of the checked out or reserved time")
        plt.show()

        # Recommend similar books to the most popular one
        most_popular_title = df.iloc[0]['Title']
        recommended_titles = set(get_recommendations(most_popular_title))
        print(f"For the most popular book '{most_popular_title}', the following are recommended:")
        print(recommended_titles)
    else:
        messagebox.showerror("Error", "Please enter a budget amount above 10£ within Library's budget range")
