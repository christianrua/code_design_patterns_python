from typing import NewType

class CodeBuilder:
    def __init__(self, root_name):
        self.class_name = root_name
        self.class_fields = []



    def infer_typing_type(type):
        if int(type):
            return int(type)
        else:
            return type    


    def add_field(self, type, name):
        
        self.name = infer_typing_type(type)
        self.class_fields.append(self.name)
        return self 

    def __str__(self):
        return f"class name {self.class_name}, class fields {self.class_fields}"
        
cb = CodeBuilder('Person').add_field('name',str).add_field('age',int)
