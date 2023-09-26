import mysql.connector
import json

class DataProcessor:

    db_server = "3306"
    db_connection = mysql.connector.connect(host="localhost",user="root",password="Singh321")

    def __init__ (self):
        self.db_connection = mysql.connector.connect(host="localhost",user="root",password="Singh321")


    def get_data_from_garden_calender_table(self,zone):
        db_pointer = self.db_connection.cursor()
        db_pointer.execute("select * from gardening_project.gardening_material;")
        data_set = db_pointer.fetchall()
        return data_set


data_processor= DataProcessor()
z8_garden_calender_data = data_processor.get_data_from_garden_calender_table('z8')
print("***********************Print Resultset from SQL ****************************************")
for each in z8_garden_calender_data:
    print(each)


# Print resultset as Json
print("***************************************************************")
print("")

print("***********************Convert Resultset into JSON OBJECT****************************************")
k= json.dumps(z8_garden_calender_data)

print("***********************Print JSON OBJECT as is****************************************")
print(k)

print("***********************Convert JSON into proper JSON FORMAT****************************************")
json_object=json.loads(k)
json_formatted = json.dumps(json_object, indent=5)
print(json_formatted)