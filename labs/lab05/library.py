class Library:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def append_(self, Book):
        self.books.append(Book)

    def search(self, author):
        found = []
        for book in self.books:
            if book.author == author:
                found.append(book)
        return found

    def info(self, name):
        for book in self.books:
            if book.name == name:
                print(book)

    def delete(self, author):
        books1 = []
        for book in self.books:
            if book.author != author:
                books1.append(book)
        self.books = books1


class Book:
    def __init__(self, name, author, distr, date, isbn):
        self.name = name
        self.author = author
        self.distr = distr
        self.date = date
        self.isbn = isbn

    def __str__(self):
        return f"Книга:{self.name}\n Автор: {self.author}\n Издательство:{self.distr}\n Год публикации:{self.date}\n Номер:{self.isbn}"


def test_library():
    narciss = Book('Нарцисс и Златоуст', 'Герман Гессе', 'Издательство АСТ', '1930', '978-5-17-119214-3')
    steppenwolf = Book('Степной Волк', 'Герман Гессе', 'Издательство АСТ', '1927', '978-5-17-114534-6')
    sidhartha = Book('Сиддхартха', 'Герман Гессе', 'Издательство АСТ', '1922', '978-5-17-114543-7')
    math = Book('Введение в вычислительную математику', 'Виктор Рябенький', '2008', 'ФИЗМАТЛИТ', '978-5-9221-0926-0')
    library = Library('Московская библиотека', [])
    library.append_(narciss)
    library.append_(steppenwolf)
    library.append_(sidhartha)

    for book in library.books:
        name = book.name
        library.info(name)
    library.delete('Герман Гессе')
    for book in library.books:
        name = book.name
        library.info(name)


if __name__ == '__main__':
    test_library()