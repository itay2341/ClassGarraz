
class Employee():
    def __init__(self, _name , _id):
       self.name=_name
       self.id=_id

    def __str__(self):
        return (f'Name:{self.name}\nID:{self.id}')

    def getEmpData(self):
        return {"Name":self.name,"ID":self.id}  