
import os as nt
from Garage import Garage

def main():
    nt.system('cls')
    myGarage=Garage("MyGarage")
    myGarage.loadingData()
    while(True):
        print("------------------------")
        print("a----add an employee")
        print("a2----add Car for Treatment")
        print("f----Finish the Treatment")
        print("p----printing")
        print("m----how much money the bank has")
        print("n----name of the Garage")
        print("x----exit")

        userselection=input("enter your choise")
        nt.system('cls')
        if(userselection=='x'):
            myGarage.savingData()
            return
        if(userselection=='a'):myGarage.addAnemployee(input("enter your name"))
        if(userselection=='a2'):myGarage.addCarToATratment(input("name of the car?"),int(input("model?")),input("color?"))
        if(userselection=='p'):
            print("1-------list of the all Employees")
            print("2-------list of the UnFinished Orders")
            print("3-------list of the Finished Orders")
            print("4-------list of the all Cars")
            userselection2=input("enter your choise")
            nt.system('cls')
            if userselection2=='1':myGarage.printEmployees()
            if userselection2=='2':myGarage.printTreatmentsInProgress()
            if userselection2=='3':myGarage.printFinishedOrders()
            if userselection2=='4':myGarage.printAllcars()
        if(userselection=='f'):myGarage.finishingTheOrder(int(input("ID?")))
        if(userselection=='m'):print(myGarage.money)
        if(userselection=='n'):myGarage.printGarage()


if   __name__ == '__main__':
    main()
