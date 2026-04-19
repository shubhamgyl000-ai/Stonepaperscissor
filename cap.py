# LIBRARY of BOOKS PROJECT.PY
books = ['Shubham_returns','Berseck of gluttony','Alia hides her feelings in russian','Next door']
issued_books = []

#ADD_BOOKS
def add_book():
    name = input("Enter the name of the book: ")
    books.append(name)
    print(f"{name} has been added to the library.")

#SHOW_BOOKS
def show_books():
    if len(books) == 0:
        print("No books available.")
    else:
        print("Books available in the library:")
        for b in books:
            print(b)
#ISSUE_BOOKS
def issue_books():
    name = input("enter the name of the book : ")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print(f"{name} has been issued.")
    else:
        print("BOOK IS NOT ISSEUED !")
#RETURN_BOOKS 
def return_books():
    name = input("enter the name of the book : ")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print(f"{name} has been returned.")
    else:
        print("BOOK IS NOT RETURNED !")   
# MAIN BODY
def library():
    print("1. Add a book")
    print("2. Show Books")
    print("3. Issue Books")
    print("4. Return Books")
    print("5. Exit")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_book()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("Thank you for using the library system!")
            break
        else:
            print("Invalid choice !")
library()
        
