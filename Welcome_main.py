from authorclass import Author, Author_ops
from bookclass import Book, Book_ToDos
from club_memberclass import Member, Member_ops



def main():
    while True:
        main_menu = input('''
Welcome to Springfield Library, located in beautiful Springfield, Oregon!
How may I help you today:

1. Book Encyclopedia
2. Springfield Book Club
3. Author Lists
4. Back to society
    ''')
        if main_menu == '1':
            book_encyclopedia()               # Open Book Encyclopedia function
        elif main_menu == "2":
            Book_club()               # Open Book Club fuction
        elif main_menu == '3':
            Author_Info()               # Open Author List
        elif main_menu == '4':
            print("Thank you for stopping by!")
            break
        else:
            print("Don't pull a Homer and please enter a valid selection.")
            continue


def book_encyclopedia():
    while True:
        book_menu = input('''
Welcome to the Book Encyclopedia, what would you like to do:

1. Add a new book
2. Rent a book
3. Return a book
4. Search the Encyclopedia 
5. Display the Encyclopedia
6. Back to main menu
    ''')
        if book_menu == '1':
            Book_ToDos.add_book()
        elif book_menu == '2':
            Book_ToDos.rent_book()
        elif book_menu == '3': 
            Book_ToDos.return_book()
        elif book_menu == '4':
            Book_ToDos.book_search()
        elif book_menu == '5':
            Book.get_info()
        elif book_menu == '6':
            return main()
        else:
            print("Don't pull a Homer and please enter a valid selection")
            continue


def Book_club():
    while True: 
        club_menu = input('''
Welcome to the Springfield Library Book Club! How can I help you friend:

1. Become a member
2. Search for a member
3. Display full member list
4. Back to main menu                         
    ''')
        if club_menu == '1':
            Member_ops.add_member()
        elif club_menu == '2':
            Member_ops.member_search()
        elif club_menu == '3': 
            Member.get_info()
        elif club_menu == '4':
            return main()
        else:
            print("Don't pull a Homer and please enter a valid selection")
            continue

def Author_Info():
    while True: 
        author_menu = input('''
Welcome to our Signature author list! What can I do for you:

1. Add a new author
2. Search for an author
3. Display full author list
4. Back to main menu                         
    ''')
        if author_menu == '1':
            Author_ops.add_author()
        elif author_menu == '2':
            Author_ops.author_search()
        elif author_menu == '3': 
            Author.get_info()
        elif author_menu == '4':
            return main()
        else:
            print("Don't pull a Homer and please enter a valid selection")
            continue
        

main()