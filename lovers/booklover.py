import pandas as pd
import numpy as np

class BookLover:
    num_books = 0
    book_list = pd.DataFrame({'book_name':[],'book_rating':[]})
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        
    def add_book (self, book_name, rating):
        if self.has_read(book_name):
            print("Book already exists") 
        else:
            new_book = pd.DataFrame({
                'book_name':[book_name],
                'book_rating':[rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            
    def has_read(self, book_name):
        if book_name in list(self.book_list.book_name):
            return True
        else:
            return False 
        
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list.book_rating>3]