class Library:
    def __init__(self,books,name):
        self.books=books
        self.name=name
        self.dict={}

    def display_book(self):
        print(f"The available books are:\n{self.books}")
        # for i in self.books:
        #     print(i, end=", ")
        # print()

    def lend_book(self):
        person=input("Please enter your name: ")
        want=input("Enter the book you want to lend :")
        if want in self.books:
            print("Ok, you can take it!\n")
            print("Issuing...")
            print("Successfully issued to you")
            self.dict[want]=person
            self.books.remove(want)
        elif want in self.dict:
            taker=self.dict[want]
            print(f"Sorry! it is already taken by {taker}")
        else:
            print("Sorry! we don't have such a book")

    def add_book(self):
        new=input("Hey Admin! Enter the book which you want to add: ")
        if new in self.books:
            print("This book is already present! please add another book...")
        elif new in self.dict:
            print("This book is already present in our library and taken by someone")
        else:
            print("Adding....")
            self.books.append(new)
            print("Successfully added!")

    def return_book(self):
        ret=input("Enter the book name: ")
        if ret in self.dict:
            self.dict.pop(ret)
            self.books.append(ret)
            print("Successfully returned")
        elif ret in self.books:
            print("You have not issued it!")
        else:
            print("We dont have such books!")

    def search_book(self):
        find = input("Enter book name to check whether it is available or not: ")
        print("Searching...")
        if find in self.books:
            print("oh! great, this book is available in our library.")
        elif find in self.dict:
            print("This book is available in our library but currently issued by someone plz wait until its available for you...")
        else:
            print("sorry we don't have such books!")

name = "\n***  Welcome To the Anupam Library  ***"

l1=Library(["Python", "java", "C", "C++", "NodeJS", "Web Dev", "javascript"],name)
print(l1.name)

while True:
    inp=(input("\nenter 1 to display books: \nenter 2 to lend a book: \nenter 3 to add a new book: \nenter 4 to return a book: \nenter 5 to search a book: \nenter 6 to exit: \n"))
    if inp == '1' or inp == 'D' or inp == 'd':
        l1.display_book()
    elif inp == '2' or inp == 'L'  or inp == 'l':
        l1.lend_book()
    elif inp == '3' or inp == 'A' or inp == 'a':
        l1.add_book()
    elif inp == '4' or inp == 'R' or inp == 'r':
        l1.return_book()
    elif inp == '5' or inp == 'S' or inp == 's':
        l1.search_book()
    elif inp == '6' or inp == 'E' or inp == 'e':
        print("\t\t *** Thanks for Using our facility! ***")
        break
    else:
        print("Invalid input!")