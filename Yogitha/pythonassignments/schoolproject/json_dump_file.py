import json

import mysql.connector


class DataProcessor:
    country = "null"
    db_server = "3306"
    db_connection = mysql.connector.connect(host="localhost", user="root", password="admin20")

    def __init__(self):
        self.db_connection = mysql.connector.connect(host="localhost", user="root", password="admin20")

    def get_data_from_country(self, country):
        db_pointer = self.db_connection.cursor()
        db_pointer.execute(f'''select city_id, city, country_id from sakila.city where country_id = (select country_id from sakila.country
where country = '{country}');''')
        data_set = db_pointer.fetchall()
        return data_set

    def convert_data(self, data_to_process):
        city_name_map = {}
        country = {"city": "India"}
        city_name_map.update(country)
        for each_row in data_to_process:
            city_name_map[each_row[0]] = each_row[1]
        return city_name_map


data_processor = DataProcessor()
city_data_for_country = data_processor.get_data_from_country("India")
city_data = data_processor.convert_data(city_data_for_country)
city_data_json = json.dumps(city_data, indent=4)
print(city_data_json)
