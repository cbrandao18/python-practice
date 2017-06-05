class book_depot:
    def __init__(self, name, location, books=[]):
        self.name = name
        self.location = location
        self.books = books
    def __str__(self, name, books):
        num = len(self.books)
        return "Name: " + name + ". Number of books: " + str(num)
    def acquire(self, book):
        if book not in self.books:
            self.books.append(book)
    def checkout(self, book):
        if book in self.books:
            self.books.remove(book)
    def find(self, book):
        if book in self.books:
            return True
        else:
            return False
    def inventory(self):
        i = 1
        num = len(self.books)
        while i-1 < num:
            print str(i) + ". " + self.books[i-1]
            i = i + 1 
    def checkin(self, book):
        if book not in self.books:
            self.books.append(book)
            

