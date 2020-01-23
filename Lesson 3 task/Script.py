import csv
import json
from context_manager_methods import ClassContextManager

cm_obj = ClassContextManager()

result = []
books = cm_obj.books_csv_reader()

for each_user in cm_obj.users_json_reader():

    book_info = next(books)
    result.append({
        "name": each_user['name'],
        "gender": each_user['gender'],
        "address": each_user['address'],
        "books": {
            "title": book_info[0],
            "author": book_info[1],
            "height": book_info[3]
        }
    })

cm_obj.output_json_writer(result)
