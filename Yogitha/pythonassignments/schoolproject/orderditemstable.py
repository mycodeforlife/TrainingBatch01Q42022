import mysql.connector


class Dataprocessor:

    db_server = "3306"
    db_connection = mysql.connector.connect(host="Localhost", user="root", password="admin20")

    def __init__(self):
        self.db_connection = mysql.connector.connect(host="Localhost", user="root", password="admin20")

    def get_orderditemstable_info(self, orderno):
        select_query = "select * from foodorderingsystem.OrderditemsTable where OrderID='"+orderno+"';"
        print(select_query)
        db_pointer = self.db_connection.cursor()
        db_pointer.execute(select_query)
        data = db_pointer.fetchall()
        return data


db = Dataprocessor()
print("printing orderditemstable details")
order_data_set = db.get_orderditemstable_info("A1")
for each_data in order_data_set:
    print("printing order details")
    print(each_data)
print()
order_data_set1 = db.get_orderditemstable_info("B5")
for each_data in order_data_set1:
    print("printing order details")
    print(each_data)
print()
order_data_set2 = db.get_orderditemstable_info("C3")
for each_data in order_data_set2:
    print("printing order details")
    print(each_data)

