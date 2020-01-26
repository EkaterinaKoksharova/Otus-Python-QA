import csv
import json

class ClassContextManager:

    pathcsv = 'Data/books.csv'
    pathjson = 'Data/users.json'
    pathjson_output = 'output.json'

    def books_csv_reader(self):
        """ Read data from a CSV file """

        with open(self.pathcsv, "r") as books:
            csvreader = csv.reader(books)
            next(csvreader)
            for row in csvreader:
                yield row

    def users_json_reader(self):
        """ Read data from a JSON file """

        with open(self.pathjson, "r") as users:
            jsonreader = json.load(users)
            for each_user in jsonreader:
                yield each_user

    def output_json_writer(self, result):
        """ Write data to a JSON file """

        with open(self.pathjson_output, "w") as books_and_users:
            json.dump(result, books_and_users, indent=4)
            