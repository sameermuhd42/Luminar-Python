class Book:
    books = {
        'alchemist': {'book_name': 'alchemist', 'author': 'paulo', 'price': 200, 'av_copies': 100, 'sold': 10},
        'halfgirlfriend': {'book_name': 'hgf', 'author': 'chethan', 'price': 300, 'av_copies': 300, 'sold': 200},
        'rainrising': {'book_name': 'rainrising', 'author': 'nirupama', 'price': 350, 'av_copies': 0, 'sold': 320}
    }

    def find_book(self, **kwargs):
        author = kwargs.get("author")
        print(self.books["alchemist"]["author"])
        if author in self.books:
            if author == self.books["author"]:
                print(self.books["book_name"])
        else:
            print("No books")


b1 = Book()
b1.find_book(author="paulo")
