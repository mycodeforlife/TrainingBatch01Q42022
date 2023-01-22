import json

from io import StringIO
str_io_obj = StringIO()

### Use JSON Dump to make StringIO

json.dump(["Armenia", "Australia", "Brazil"], str_io_obj)
print('StringIO Object value: ' + str(str_io_obj.getvalue()))
my_json = {
    "Name": "NICK",
    "actor_id": "2",
    "last_update": "2006-02-15 04:34:33"
}
print(json.dumps(my_json))







