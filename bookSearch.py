import database



def SearchBook(search_book):
    """
    The function to search Books based on the Book name

    Parameters : 
    search_book : Bookname entered by the user 

    Returns :
    rows : All the Books which has the same Title along with their
           author,genre,title,Book id and status


    """
    conn,cur = database.db_connection()
    query = "Select * from BOOKLIST where title like '%"+search_book+"%'"
    cur.execute(query)
    rows = cur.fetchall()
    return rows


print(SearchBook.__doc__)

