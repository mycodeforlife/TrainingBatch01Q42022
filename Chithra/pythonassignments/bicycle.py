
class Bicycles:

    bicycle_manufacture_name = ""
    bicycle_color = ""

    def __init__(self,bicycle_name):
        self.bicycle_name = bicycle_name

    def bicycle_detials(self, bicycle_type, color, bicycle_user,wheelsize_inches):
        self.bicycle_type = bicycle_type
        self.color = color
        self.bicycle_user = bicycle_user
        self.wheelsize_inches = wheelsize_inches

    def get_bicycle_name(self,bicycle_name):
        return self.bicycle_name




name = ["Trek"]
variety = ["mountain bike"]
color = ["black"]
gender_preference = ["unisex"]
