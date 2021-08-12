from typing import ContextManager


class vehicle:
    def __init__(self,reg_no,color) -> None:
        self.reg_no=reg_no
        self.color=color

class car(vehicle):
    def __init__(self,reg_no,color) -> None:
        vehicle.__init__(self,reg_no,color)
    def getType(self):
        return "Car"
