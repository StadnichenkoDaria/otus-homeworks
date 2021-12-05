from csv import DictReader
from json import loads, dumps
from itertools import cycle

result = []
with open("../data/users.json", "r") as json_file:
    with open("../data/books.csv", "r") as csv_file:
        with open("../data/result.json", "w") as write_file:
            users = loads(json_file.read())
            books = DictReader(csv_file)

            for user in users:
                user = {'name': user.get('name'), 'gender': user.get('gender'), 'address': user.get('address'),
                        'age': user.get('age'), 'books': []}
                result.append(user)

            for book, user in zip(books, cycle(result)):
                book = {'title': book.get("Title"), 'author': book.get("Author"), 'pages': int(book.get("Pages")),
                        'genre': book.get("Genre")}
                user['books'].append(book)

            write_file.write(dumps(result, indent=4))
