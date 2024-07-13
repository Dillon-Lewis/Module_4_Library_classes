# Welcome to our Signature author list! What can I do for you:

# 1. Add a new author
# 2. Search for an author
# 3. Display full author list
# 4. Back to main menu    

author_list = {
'Lisa Simpson': {'Birthdate' : '4/19/1987', "Short Bio" : 'Avid author and saxaphone player, she has devoted her later years into writing fictional love stories'},
'JJR Tolkien': { "Birthdate ": '1/3/1892', "Short Bio" : 'English writer famously known for his fantasy works like the Hobbit and LOTR',}, 
'Frank Herbert': {"Birthdate": '11/8/1920', "Short Bio" : " American sci-fi writer with a rich history in short stories and newspaper articles"}
}
  

class Author():
    def __init__(self, name, birth_date, short_bio):
        self.name = name
        self.birth_date = birth_date
        self.short_bio = short_bio

    def set_name(self, new_name):
        self.name =  new_name
    
    def set_birth_date(self, birth):
        self.birth_date = birth
    
    def set_short_bio(self,new_bio):
        self.short_bio = new_bio

    def get_info(self):
        print(f"{self.name} was born on/in {self.birth_date}. {self.short_bio}")

class Author_ops():
     
    def __init__(self):
        self.authors =[]

    def add_author(self):
        name = input("What is there name? ").title()
        birth_date= input("When were they born? ").title()
        short_bio= input("Give me a little information on them? ")
        self.name = name
        self.birth_date = birth_date
        self.short_bio = short_bio
        add_author = Author(name, birth_date, short_bio)
        self.authors.append(add_author)

    def author_search(self):
        while True:
            search = input("Please enter the name of the author you are searchin for:  ").title()
            for author in self.authors:
                if search == author.name:
                    print(f"{author.name} was born on/in {author.birth_date}. {author.short_bio}")
            print("Author not found, try again.")
            break
