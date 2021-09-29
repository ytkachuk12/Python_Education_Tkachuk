"""Learning oop"""

from abc import ABC, abstractmethod


class Fuel(ABC):
    """Abstract class of fuel stations"""
    @abstractmethod
    def __str__(self):
        pass


class Gasoline(Fuel):
    """gasoline charge station"""
    fuel_type: str = "gas"

    def __init__(self, charge):
        self.charge = charge

    def __str__(self):
        return f"Here you can refill by {self.fuel_type}"


class Diesel(Fuel):
    """diesel charge station"""
    fuel_type: str = "diesel"

    def __init__(self, charge):
        self.charge = charge

    def __str__(self):
        return f"Here you can refill by {self.fuel_type}"


class Electric(Fuel):
    """electric charge station"""
    fuel_type: str = "electric"

    def __init__(self, charge):
        self.charge = charge

    def __str__(self):
        return f"Here you can refill by {self.fuel_type}"


class Tank:
    """fuel type, volume of tank, and level of fuel in tank"""
    def __init__(self, fuel_type: str, fuel_tank: int, fuel_level: int):
        self.fuel_tank = fuel_tank
        self.fuel_type = fuel_type
        self.fuel_level = fuel_level

    def __add__(self, other):
        if isinstance(other, (Gasoline, Diesel, Electric)):
            if self. fuel_type == other.fuel_type:
                self.fuel_level = self.fuel_level + other.charge
                return f"Transport refilled on {other.charge} \
                and now in tank {self.fuel_level}"
        return f"Transport needs {other.fuel_type} fuel type\
        and now in tank {self.fuel_level}"

    @property
    def start_engine(self):
        """check fuel level and start engine"""
        if self.fuel_level > 0:
            print(f"Class print. Engine start: tank has {self.fuel_level}")
            return True
        print("Something wrong")
        return False

    @start_engine.setter
    def start_engine(self, fuel_level: int):
        """set fuel level"""
        print("вызов __set_engine")
        self.fuel_level = fuel_level


class Engine:
    """Engine power, volume, fuel, turbine """

    def __init__(self, power: int, volume: int, turbine: bool, *args):
        self.power = power
        self.volume = volume
        self.turbine = turbine
        super().__init__(*args)

    @staticmethod
    def stop_engine():
        """just stop"""
        print("stop")


class Transport:
    """#Year, brand, color, seats, carrying_capacity"""
    wheels = 4
    # like data base
    brand_db = ["renault", "mazda", "tesla"]

    def __init__(self, brand: str, color: str, year: int, seats: int, *args):
        self.brand = brand
        self.color = color
        self.year = year
        self.seats = seats
        super().__init__(*args)

    @classmethod
    def get_wheels(cls):
        """wheels param"""
        return f"Your vehicle has {cls.wheels} wheels"

    def __eq__(self, other):
        if isinstance(other, Transport):
            return self.year == other.year
        return f"not the same year of production {self.year} and {other.year}"

    def __contains__(self, item):
        if item in self.brand_db:
            print("brand in DB")
        self.brand_db.append(item)
        print("added brand in DB")


class Car(Transport, Engine, Tank):
    """car, child class """
    allowed_drivers_license = "Type B"

    def __init__(self, *args):
        super().__init__(*args)

    def drive(self):
        print(f"You can drive, cause you have {Car.allowed_drivers_license} driver's license")
        super().drive()


class Bus(Transport, Engine, Tank):
    """bus, child class"""

    allowed_drivers_license = "Type D"

    def __init__(self, *args):
        super().__init__(*args)

    def drive(self):
        print(f"You can drive, cause you have {Bus.allowed_drivers_license} driver's license")


class MiniVan(Car, Bus):

    allowed_drivers_license = "Type D1"

    def drive(self):
        print(f"You can drive, cause you have {MiniVan.allowed_drivers_license} driver's license")
        super().drive()

    def another_drive(self):
        super(Bus).drive()


class Truck(Transport, Engine, Tank):
    """truck child class"""
    wheels = 6

    max_carrying_capacity = 10000
    min_carrying_capacity = 3000

    def set_carrying(self, carrying_capacity):
        """set carrying capacity between min and max"""
        if Truck.validate_carrying(carrying_capacity):
            self.carrying_capacity = carrying_capacity
            return f"your carrying cap is {self.carrying_capacity}"
        return f"min carrying capacity is {self.min_carrying_capacity} \
        and max is {self.max_carrying_capacity}"

    @classmethod
    def validate_carrying(cls, arg):
        """check that capacity between min and max"""
        if cls.min_carrying_capacity <= arg <= cls.max_carrying_capacity:
            return True
        return False

    @classmethod
    def get_wheels(cls):
        """wheels param"""
        return f"Your vehicle has {cls.wheels} wheels"


class Bike(Transport, Engine, Tank):
    """bike child class"""
    wheels = 2

    @classmethod
    def get_wheels(cls):
        """wheels param"""
        return f"Your vehicle has {cls.wheels} wheels"


if __name__ == "__main__":
    # charge
    gas_charge = Gasoline(35)
    print(gas_charge)
    diesel_charge = Diesel(50)

    print()
    # Tank fuel_type: str, fuel_tank: int, fuel_level: int
    car_tank = Tank("gas", 60, 0)
    truck_tank = Tank("diesel", 450, 0)

    # power: int, volume: int, turbine: bool = False
    car_eng = Engine(120, 2102, True)
    truck_eng = Engine(560, 20750, True)
    print(car_eng, car_eng.power)
    car_eng.stop_engine()

    print()
    # brand: str, color: str, year: int, seats: int
    tran = Transport("renault", "red", 2011, 3)
    print(tran, tran.brand)
    tran2 = Transport("mazda", "blue", 2011, 5)
    print(tran == tran2)

    print()
    truck = Truck("renault", "red", 2011, 3, 560, 20750, False, "diesel", 450, 0)
    print(Truck.get_wheels())
    print(truck.set_carrying(1500))
    print(truck + gas_charge)
    print(truck + diesel_charge)
    truck + diesel_charge
    truck.start_engine
    truck.start_engine = 30
    truck.start_engine

    print()
    mini_van = MiniVan("renault", "red", 2011, 9, 560, 20750, False, "diesel", 450, 0)
    mini_van.drive()
