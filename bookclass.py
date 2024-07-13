# Welcome to the Book Encyclopedia, what would you like to do:

# 1. Add a new book
# 2. Borrow/Rent a book
# 3. Return a book
# 4. Search the Encyclopedia 
# 5. Display the Encyclopedia
# 6. Back to main menu

Book_list = {
'Dune': {"author" : 'Frank Herbert', "Genre": 'Science Fiction', "Summary" : 'The battle for spice is on and there can only be one victor in charge of the spice fields', "Available" : 'YES'},
'The Hobbit': {"author" :  'JRR Tolkien', 'Genre' : 'Fantasy', 'Summary' : 'A group of friend must travel through Middle Earth to defeat a dragon and save the Dwarven Homeland','Available': 'YES'},
'Saxaphonie': {"author": 'Lisa Simpson', 'Genre': 'Romance', 'Summary' : 'A women falls in love wiht an Orchestrator that has a hidden past that slow becomes revieled', 'Available' : 'YES'}                
    }

class Book():
    

    def __init__(self, title, author, genre, summary):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = "Available"

    def set_title(self, new_title):
        self.title =  new_title
    
    def set_author(self, author):
        self.author = author
    
    def set_genre(self,new_genre):
        self.genre = new_genre

    def get_info(self):
        print(f"{self.title} by {self.author} ")

class Book_ToDos():
    def __init__(self):
        self.books =[]
        self.rented = []

    def add_book(self):
        title = input("What is the title of the book? ").title()
        Author= input("Who wrote the book?  ").title()
        genre= input("What genre would you list it under?  ").title()
        self.title = title
        self.author = Author
        self.genre = genre
        added_book = Book(title, Author, genre)
        self.books.append(added_book)

    def rent_book(self):
        while True:
            rental = input("Please enter the title of the book you would like to rent? ").title()
            for book in self.books:
                if  rental == book.title and book.availability  ==  "Available":
                    book.availability = "Out"
                    self.rented.append(book)
                    return
            print("The book is currently unavailable for rent.")

    def return_book(self):
        rental = input("What book are you trying to return?  ").title()
        for book in self.books:
            if rental == book.title and book.availability == "Available":
                print("Umm that is not one of our books. ")
                return
            if rental == book.title and book.availability == "Out":
                book.availability = "Available"
                self.rented.remove(book)
                print("Thank you for returning your book!")
        print("There are no books that are in our database named that.")
    
    def book_search(self):
        while True:
            search = input("Enter the title of the book you are looking for:  ").title()
            for book in self.books:
                if search == book.title:
                    print(f"{book.title} by {book.author} is currently {book.availability} for rent. ")
            print("Book not found, try again")
            break
        
