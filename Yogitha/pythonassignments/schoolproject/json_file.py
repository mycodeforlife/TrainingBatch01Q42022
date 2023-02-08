import json

import mysql.connector


class DataProcessor:
    country = "null"
    db_server = "3306"
    db_connection = mysql.connector.connect(host="localhost", user="root", password="admin20")

    def __init__(self):
        self.db_connection = mysql.connector.connect(host="localhost", user="root", password="admin20")

    def get_data_from_country(self, country):
        # select city_id,city from sakila.city where country_id = "44"
        # select country_id from sakila.country where country = "India"
        # get_country_id_query = "select country_id from sakila.country where country = \""+country+"\""
        # get_city_info_query =
        db_pointer = self.db_connection.cursor()
        db_pointer.execute(f'''select city_id, city, country_id from sakila.city where country_id = (select country_id from sakila.country
where country = '{country}');''')
        data_set = db_pointer.fetchall()
        return data_set

    def convert_data(self, data_to_process, country_name):
        data_set = {}
        data_set["Country"] = country_name
        list_of_cities_dict = []
        for each_city_info in data_to_process:
            temp_data_map = {}
            print(each_city_info[0], each_city_info[1])
            temp_data_map["CityName"] = each_city_info[1]
            temp_data_map["CityId"] = each_city_info[0]
            list_of_cities_dict.append(temp_data_map)

        data_set["City"] = list_of_cities_dict
        return data_set


data_processor = DataProcessor()
list_of_countries = ["India", "United states"]
country_city_data_list = []
for country in list_of_countries:
    city_data_for_country = data_processor.get_data_from_country(country)
    country_city_data = data_processor.convert_data(city_data_for_country, country)
    country_city_data_list.append(country_city_data)


print(country_city_data_list)



