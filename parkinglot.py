from typing import SupportsFloat
import vehicle
import argparse

class parkinglot:
    def __init__(self) -> None:
        self.capacity=0
        self.slotid=0
        self.numberofoccupiedslot=0

    def createparkinglot(self,capacity):
        self.slots = [-1]*capacity
        self.capacity = capacity        
        return self.capacity
    
    def get_empty_slot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, reg_no,color):
        if self.numberofoccupiedslot < self.capacity:
            slotid = self.get_empty_slot()
            self.slots[slotid] = vehicle.car(reg_no,color)
            self.slotid += 1
            self.numberofoccupiedslot +=1
            return slotid+1
        else:
            return -1

    def leave(self,slotid):
        if self.numberofoccupiedslot > 0 and self.slots[slotid-1]!=-1:
            self.slots[slotid-1] = -1
            self.numberofoccupiedslot -=1
            return True
        else:
            return False

    def status(self):
        print(len(self.slots))
        print("slot No. \tRegistration No. \tcolor")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i+1)+"\t\t"+self.slots[i].reg_no+"\t\t"+self.slots[i].color )
            else:
                continue

    def getRegNoFromColor(self,color):
        regnos=[]
        for i in self.slots:
            if i==-1:
                continue
            if i.color == color:
                regnos.append(i.reg_no)
        return regnos

    def getSlotNoFromRegNo(self,regno):        
        for i in range(len(self.slots)):            
            if self.slots[i].reg_no == regno:
                return i+1
            else:
                continue
        return -1

    def getslotNoFromColor(self,color):
        slotsnos=[]
        for i in range(len(self.slots)):
            if self.slots[i]==-1:
                continue
            if self.slots[i].color == color:
                slotsnos.append(str(i+1))
        return slotsnos
    
    def show(self,line):
        if line.startswith('create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.createparkinglot(n)
            print("created parking lot with "+str(res)+" slots")
        elif line.startswith('park'):
            regno= line.split(' ')[1]
            color= line.split(' ')[2]
            res = self.park(regno,color)
            if res == -1:
                print("sorry parking lot is full")
            else:
                print("alloted slot number: "+str(res))
        elif line.startswith('leave'):
            leave_slotid= int(line.split(' ')[1])
            status = self.leave(leave_slotid)
            if status:
                print("slot number "+ str(leave_slotid)+ " is free")
        elif line.startswith('status'):
            print(self.status())

        elif line.startswith('registration_number_for_cars_with_colour'):
            color = line.split(' ')[1]
            regnos = self.getRegNoFromColor(color)
            print(', '.join(regnos))

        elif line.startswith('slot_number_for_cars_with_colour'):
            color = line.split(' ')[1]
            slotnos = self.getslotNoFromColor(color)
            print(', '.join(slotnos))
        
        elif line.startswith('slot_number_with_registration_number'):
            regno = line.split(" ")[1]
            slotno = self.getSlotNoFromRegNo(regno)
            if slotno==-1:
                print ("not found")
            else:
                print(slotno)
        elif line.startswith('exit'):
            exit(0)
def main():
    Parkinglot = parkinglot()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',action="store",required=False,dest="src_file",help="input_file")
    args = parser.parse_args()
    if args.src_file:
        with open(args.src_file) as f:
            for line in f:
                line = line.rstrip("\n")
                Parkinglot.show(line)
    else:
        while True:
            line = input("$")
            Parkinglot.show(line)
if __name__=='__main__':
    main()
