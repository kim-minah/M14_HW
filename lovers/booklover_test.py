import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        bl = BookLover('name','email','fantasy')
        bl.add_book('Nisa',4)
        self.assertIn('Nisa',list(bl.book_list['book_name']),"Book was not added")

    
    def test_2_add_book(self):
        bl = BookLover('name','email','fantasy')
        bl.book_list = pd.DataFrame({'book_name':['Nisa'],'book_rating':[4]})
        bl.add_book('Nisa',4)
        
        expected = 1
        nisa_entries = len(bl.book_list[bl.book_list.book_name=='Nisa'])
        self.assertEqual(nisa_entries,expected)

    def test_3_has_read(self): 
        bl = BookLover('name','email','fantasy')
        bl.book_list = pd.DataFrame({'book_name':['Nisa'],'book_rating':[4]})
        self.assertTrue(bl.has_read("Nisa"),"Test value is not True")
        
    def test_4_has_read(self): 
        bl = BookLover('name','email','fantasy')
        bl.book_list = pd.DataFrame({'book_name':['Nisa'],'book_rating':[4]})
        self.assertFalse(bl.has_read("Spiderman"),"Test value is not False")
                     
    def test_5_num_books_read(self): 
        bl = BookLover('name','email','fantasy')
        bl.add_book("Nisa",4)
        bl.add_book("Spiderman",3)
        bl.add_book("It",2)
        
        expected = 3
        self.assertEqual(bl.num_books_read(), expected)

    def test_6_fav_books(self):
        bl = BookLover('name','email','fantasy')
        bl.add_book("Nisa",4)
        bl.add_book("Spiderman",3)
        bl.add_book("It",2)
        bl.add_book("Holes",5)
        
        fav_ratings = bl.fav_books().book_rating.values
        self.assertTrue((fav_ratings > 3).all)
        #self.assertGreater(bl.fav_books().book_rating.values,3)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)       