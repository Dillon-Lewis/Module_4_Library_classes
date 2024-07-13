# Welcome to the Springfield Library Book Club! How can I help you friend:

# 1. Become a member
# 2. Search for a member
# 3. Display full member list
# 4. Back to main menu             

class Member():

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.current_rentals = 0

   
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name

    def get_id(self):
        return self.__user_id
    def set_id(self, new_id):
        self.user_id = new_id
    
    def get_info(self):
        print(f"{self.name} at user ID: {self.user_id} currently has {self.current_rentals} out on rent!")
        

class Member_ops():
     
    def __init__(self):
        self.members =[]

    def add_member(self):
        name = input("What is your name? ").title()
        user_id= int(input("Please enter your phone number with no spaces or dashes"))
        self.name = name
        self.user_id = user_id
        add_member = Member(name, user_id)
        self.members.append(add_member)

    def member_search(self):
        while True:
            search = input("Please enter the name of the user you are searchin for:  ").title()
            for member in self.members:
                if search == member.name:
                    print(f"{member.name}, currently has {member.availability} on rental.")
            print("User not found, try again.")
            break

    
    

