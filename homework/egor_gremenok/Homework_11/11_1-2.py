class Book:
    material = "бумага"
    text = True

    def __init__(self, title, author, size, isbn, reserve):
        self.title = title
        self.author = author
        self.size = size
        self.isbn = isbn
        self.reserve = reserve


class Textbook(Book):
    tests = True

    def __init__(self, title, author, size, isbn, reserve, subject, grade):
        super().__init__(title, author, size, isbn, reserve)
        self.subject = subject
        self.grade = grade


def check_books(books_list):
    print("Книги:")
    for book in books_list:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.size}, материал: {book.material}", end="")
        if book.reserve is True:
            print(", зарезервирована")
        else:
            print()


def check_textbooks(books_list):
    print("Учебники:")
    for book in books_list:
        print(f"Название: {book.title}, Автор: {book.author}, страниц: {book.size}, "
              f"предмет: {book.subject}, класс: {book.grade}", end="")
        if book.reserve is True:
            print(", зарезервирована")
        else:
            print()


book1 = Book("Автостопом по галактике", "Д. Адамс", 424, 577692356925, False)
book2 = Book("Идиот", "Ф. Достоевский", 500, 835615346972, True)
book3 = Book("1984", "Д. Оруэлл", 384, 947564018343, False)
book4 = Book("Властелин колец", "Д. Р. Р. Толкин", 682, 857644381290, False)
book5 = Book("Война и мир", "Л. Толстой", 983, 890123489541, True)

books = [book1, book2, book3, book4, book5]
check_books(books)
print()

textbook1 = Textbook("Алгебра. 9 класс", "Иванов", 200, 123123123123,
                     False, "Алгебра", 9)
textbook2 = Textbook("Физика. 10 класс", "Петров", 350, 564654654654,
                     True, "Физика", 10)
textbook3 = Textbook("Химия. 7 класс", "Сидоров", 180, 754754754754,
                     False, "Химия", 7)
textbook4 = Textbook("История. 11 класс", "Кузьминов", 220, 934934934934,
                     False, "История", 11)
textbook5 = Textbook("Русский язык. 8 класс", "Синицына", 275, 358358358358,
                     False, "Русский язык", 8)

textbooks = [textbook1, textbook2, textbook3, textbook4, textbook5]
check_textbooks(textbooks)
