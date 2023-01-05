class FileExtensionUpdate:

    def __init__(self,file_name_list):
        self.filenames = file_name_list
       # print("hello i am inside creating initial data/object for class")

    def update_extension(self):
        new_file_names = []
        for filename in self.filenames:
            if filename.endswith(".app"):
                filename = filename.replace(".app",".a")
                new_file_names.append(filename)
            else:
                new_file_names.append(filename)
        self.filenames = new_file_names

    def get_updated_file_names(self):
        return self.filenames


external_file_name_list = ["program.c","studio.app","sample.app","a.out","math.app","app.out"]
external_file_name_list_copy2 = ["program.app","studio.app","sample.app","a.app","math.app","header_file.app"]

file_extension_change = FileExtensionUpdate(external_file_name_list)
file_extension_change1 = FileExtensionUpdate(external_file_name_list_copy2)
file_extension_change.update_extension()
file_extension_change1.update_extension()
updated_file_info = file_extension_change.get_updated_file_names()
updated_file_info1 = file_extension_change1.get_updated_file_names()
print(updated_file_info)
print(updated_file_info1)