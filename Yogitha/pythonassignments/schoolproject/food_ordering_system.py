import mysql.connector


class DataProcessor:

    db_server = "3306"
    db_connection = mysql.connector.connect(host="localhost", user="root", password="admin20")

    def __init__(self):
        self.db_connection = mysql.connector.connect(host="localhost", user="root", password="admin20")

    def get_employee_info(self, jtype):
        select_query = "select * from foodorderingsystem.employeetable where Jobtype ='"+jtype+"';"
        print(select_query)
        db_pointer = self.db_connection.cursor()
        db_pointer.execute(select_query)
        data = db_pointer.fetchall()
        return data

    def get_order_details(self, orderno):
        order_query = "select * from foodorderingsystem.orderstable where OrderID='"+orderno+"';"
        print(order_query)
        db_pointer = self.db_connection.cursor()
        db_pointer.execute(order_query)
        data = db_pointer.fetchall()
        return data


db = DataProcessor()
print("printing Part Time employee details")
data_set = db.get_employee_info("Part-time")
for each_data in data_set:
    print(each_data)

print("printing Full Time employee details")
data_set = db.get_employee_info("Full-time")
for each_data in data_set:
    print(each_data)
print()
print("printing orderno orderstable")
order_data_set = db.get_order_details("B5")
for each_data in order_data_set:
    print("printing order details")
    print(each_data)






