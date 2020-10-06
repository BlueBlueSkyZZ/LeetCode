class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.big -= 1
            if self.big < 0:
                return False
        elif carType == 2:
            self.medium -= 1
            if self.medium < 0:
                return False
        else:
            self.small -= 1
            if self.small < 0:
                return False
        return True

# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 0)
param_1 = obj.addCar(1)
print(param_1)
print(obj.addCar(2))
print(obj.addCar(3))
print(obj.addCar(1))