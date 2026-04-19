#~ LIBRARY .PY
books=["Shubham_returns","Marvel","Berseck of gluttony" ]
issued_books=[]
#^ ADD BOOKS
def add_books():
    name=input("Enter the books name:")
    books.append(name)
    print("Books Added")
#^ SHOW BOOKS
def show_books():
    if len(books)==0:
        print("NO BOOKS AVAILABLE")
    else:
        print("Books Available:")
        for b in books:
            print(b)
#^ ISSUE BOOKS
def issue_books():
    name=input("Enter a Book name:")
    if name in books:
        books.remove(name)
        issued_books.append(name)
        print("Book is Issued")
    else:
        print("Books not Issued")
#^ RETURN BOOKS
def return_books():
    name = input("Enter a book name:")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("Books Returned")
    else:
        print("NO BOOKS RETURNED")
           

#! MAIN BODY
def library():
    while True:
        print("1.Add Books")
        print("2.Show Books")
        print("3.Issue Books")
        print("4.Return Books")
        print("5.Exit")
        choice = int(input("Enter your choice:"))
        if choice==1:
            add_books()
        elif choice ==2:
            show_books()
        elif choice==3:
            issue_books()
        elif choice==4:
            return_books()
        elif choice==5:
            print("Thank You")
            break;
        else:
            print("Invalid Books")
            break;
library()
                        