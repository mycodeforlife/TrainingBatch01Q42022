import mysql.connector


class DataProcessor:

    db_server = "3306"
    db_connection = mysql.connector.connect(host="localhost", user="root", password="admin20")

    def __init__(self):
        self.db_connection = mysql.connector.connect(host="localhost", user="root", password="admin20")

    def get_data_from_calender(self, city):
        select_query = "SELECT city FROM sakila.city where city='"+city+"';"
        print(select_query)
        db_pointer = self.db_connection.cursor()
        db_pointer.execute(select_query)
        data = db_pointer.fetchall()
        return data


db = DataProcessor()
data_set = db.get_data_from_calender("Vijayawada")
for each_data in data_set:
    print(each_data)

