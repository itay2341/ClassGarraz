

class Order():
    def __init__(self, _nametreatment , _carID,_employeeID, _money,_id):
       self.name=_nametreatment
       self.car=_carID
       self.emp=_employeeID
       self.money=_money
       self.id=_id

    def __str__(self):
        return (f'Treatment:{self.name}\nCarID:{self.car}\nEmployee worked for(ID):{self.emp}\nThe price: {self.money} \nID:{self.id}') 

    def getOrdData(self):
        return {"Name":self.name,"CarID":self.car,"EmpID":self.emp,"Money":self.money,"ID":self.id}           

