import json

import mysql.connector


class DataProcessor:
    country = "null"
    db_server = "3306"
    db_connection = mysql.connector.connect(host="localhost", user="root", password="admin20")

    def __init__(self):
        self.db_connection = mysql.connector.connect(host="localhost", user="root", password="admin20")

    def get_data_from_producttable(self, Ptype):
        select_query = "select * from foodorderingsystem.producttable where ProductType ='"+Ptype+"';"
        print(select_query)
        db_pointer = self.db_connection.cursor()
        db_pointer.execute(select_query)
        data_set = db_pointer.fetchall()
        return data_set

    def convert_data(self, data_to_process, ProductName):
        data_set = {}
        data_set["Product"] = ProductName
        list_of_product_dict = []
        for each_product_info in data_to_process:
            temp_data_map = {}
            print(each_product_info[0], each_product_info[1])
            temp_data_map["productName"] = each_product_info[1]
            temp_data_map["productId"] = each_product_info[0]
            list_of_product_dict.append(temp_data_map)

        data_set["Product"] = list_of_product_dict
        return data_set


data_processor = DataProcessor()
list_of_products = ["veg", "'Non-veg'"]
products_data_list = []
for producttable in list_of_products:
    products_data_list = data_processor.get_data_from_producttable(producttable)
    products_data = data_processor.convert_data(products_data_list, producttable)
    products_data_list.append(products_data_list)


print(products_data_list)





