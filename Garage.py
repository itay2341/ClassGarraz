
import json
from Car import Car
from Employee import Employee
from Order import Order


class Garage():
    def __init__(self,_name):
        self.name=_name
    unfinished=[]
    finished=[]
    employees=[]
    cars=[]
    idid=0
    idid2=0
    idid3=0
    money=0

    def printGarage(self):
        print(self.name)

    def addAnemployee(self,name):
        self.idid+=1
        self.employees.append(Employee(name,self.idid))

    def addCarToATratment(self, name,model,color):
        if model>2022:return
        print("b-------------back")
        print("c-------------cleaning , price:100")
        print("p-------------pancher fix, price:200")
        print("t-------------total loss fix, price:500")
        userselection=input("enter your choise - c/p/t/b")
        if userselection=='b':return
        self.idid2+=1
        self.idid3+=10
        if userselection=='c':
            self.unfinished.append(Order("cleaning",self.idid3,self.choosingEmployee(),100,self.idid2))
            self.cars.append(Car(name,model,color,self.idid3))
        if userselection=='p':
            self.unfinished.append(Order("Pancher",self.idid3,self.choosingEmployee(),200,self.idid2))
            self.cars.append(Car(name,model,color,self.idid3))
        if userselection=='t':
            self.unfinished.append(Order("Total los",self.idid3,self.choosingEmployee(),500,self.idid2))
            self.cars.append(Car(name,model,color,self.idid3))

    def finishingTheOrder(self,id):
        i=0
        for a,x in enumerate(self.unfinished):
            if( x.id==id):
                i+=1
                self.unfinished.pop(a)
                self.finished.append(x)
                self.money+=x.money
        if i==0:print("I can't find this Order")    

    def printEmployees(self):
        for x in self.employees:
            print("------------------------")
            print(x)

    def printTreatmentsInProgress(self):
        for x in self.unfinished:
            print("------------------------")
            print(x)

    def printFinishedOrders(self):
        for x in self.finished:
            print("------------------------")
            print(x)  
 
    def printMoney(self):
        print("------------------------")
        print(self.money)    

    def printAllcars(self):
        for x in self.cars:
            print("------------------------")
            print(x)
            
    def choosingEmployee(self):
        print("------------------------")
        self.printEmployees()
        print("------------------------")
        userselection2=int(input("select by ID an employee"))
        for x in self.employees:
            if x.id==userselection2:return x.id 

    def loadingData(self):
        listdata=[]
        try:
            with open("dataGarage.json" ,"r") as f:
                listdata=json.load(f)
        except FileNotFoundError:
            print("I cant find the file") 
        except:
            print("I don't know what the fuck")   
        else:
            list4=listdata[-1]
            listdata.remove(list4)
            self.money=list4[-1]
            self.idid3=list4[-2]
            self.idid2=list4[-3]
            self.idid=list4[-4]
            carslist=listdata[-1]
            for car in carslist:self.cars.append(Car((car["Name"]),car["Model"],car["Color"],car["ID"]))
            emplist=listdata[-2]
            for emp in emplist:self.employees.append(Employee((emp["Name"]),emp["ID"]))
            finish=listdata[-3]
            for f in finish:self.finished.append(Order((f["Name"]),f["CarID"],f["EmpID"],f["Money"],f["ID"]))
            unfinish=listdata[-4]
            for u in unfinish:self.unfinished.append(Order((u["Name"]),u["CarID"],u["EmpID"],u["Money"],u["ID"]))
            print("successfully!!")
        finally:print("Let's go")
       

    def savingData(self):
        newlist=[]
        for acc in self.unfinished:newlist.append(acc.getOrdData())
        newlist1=[]
        for acc1 in self.finished:newlist1.append(acc1.getOrdData())
        emp=[]
        for acc2 in self.employees:emp.append(acc2.getEmpData())
        car2=[]
        for acc3 in self.cars:car2.append(acc3.gatCarData())
        listtofile=[newlist,newlist1,emp,car2]
        listtofile.append([self.idid,self.idid2,self.idid3,self.money])
        with open("dataGarage.json", "w") as f:
            json.dump(listtofile, f)
