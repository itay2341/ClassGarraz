

class Car():
    def __init__(self, _name , _model , _color,_id):
       self.name=_name
       self.model=_model
       self.color=_color
       self.id=_id

    def __str__(self):
        return (f'Name:{self.name}\nModel:{self.model}\nColor:{self.color}\nID: {self.id}')

    def gatCarData(self):
        return {"Name":self.name,"Model":self.model,"Color":self.color,"ID":self.id}
