class Book:
    lib_name = "ABC Library"

    def book_create(self, name, author, pages, price):
        self.name = name
        self.author = author
        self.pages = pages
        self.price = price
        print("Book added successfully!")
        print("Book Name:", self.name, "\nAuthor:", self.author, "\nNo. of Pages:", self.pages,
              "\nLibrary Name:", Book.lib_name, "\nPrice:", self.price)


book1 = Book()
bname = input("Enter the book name: ")
bauthor = input("Enter the author: ")
bpages = int(input("Enter the no.of pages:"))
bprice = int(input("Enter the price: "))
book1.book_create(bname, bauthor, bpages, bprice)

# 2 types of variables
# static variable - related to class - access using class name
# instance variable - related to methods - access using self
