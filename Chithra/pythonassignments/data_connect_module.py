import mysql.connector
import json


class DataProcessor:

    db_server = ""
    db_connection = mysql.connector.connect(host="localhost", user="root", password="*Travelmate1")

    def __init__(self):
        self.db_connection = mysql.connector.connect(host="localhost", user="root", password="*Travelmate1", database="sakila")

    def get_data_from_country(self, country):
        db_point = self.db_connection.cursor()
        db_point.execute(f'''select city_id,city from city
where country_id = (select country_id from country
where country = '{country}');''')
        data_set = db_point.fetchall()
        return data_set

    def get_all_country_data(self):
        db_point = self.db_connection.cursor()
        db_point.execute(f'''select country_id,country from country''')
        country_data_set = db_point.fetchall()
        country_map = {}
        for country in country_data_set:
            city_map = {}
            db_point = self.db_connection.cursor()
            db_point.execute(f'''select city_id,city from city where country_id =  {country[0]}''')
            city_data_set = db_point.fetchall()
            for city in city_data_set:
                city_map[city[0]] = city[1]
            country_map[country[1]]  =  city_map

        return country_map

    def convert_data(self, data_to_process):
        city_name_map = {}
        for each_row in data_to_process:
            city_name_map[each_row[0]] = each_row[1]
        return city_name_map

    # def write_newCountry(self, country):
    #     db_point = self.db_connection.cursor()
    #     insert_query = "INSERT into sakila.country(country) value (\"ABDC\");"
    #     db_point.execute(insert_query)
    #     self.db_connection.commit()


data_processor = DataProcessor()

city_data_for_country = data_processor.get_data_from_country("India")
city_data = data_processor.convert_data(city_data_for_country)
city_data_json = json.dumps(city_data_for_country)
# data_processor.write_newCountry("ABDCED")
all_data = data_processor.get_all_country_data()
print(json.dumps(all_data))

