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
        print(f"Your engine needs {self.fuel_type}")


class Diesel(Fuel):
    """diesel charge station"""
    fuel_type: str = "diesel"

    def __init__(self, charge):
        self.charge = charge

    def __str__(self, charge):
        print(f"Your engine needs {Diesel.fuel_type}")


class Electric(Fuel):
    """electric charge station"""
    fuel_type: str = "electric"

    def __init__(self, charge):
        self.charge = charge

    def __str__(self):
        print(f"Your engine needs {Diesel.fuel_type}")


class Tank:
    def __init__(self, fuel_type: str, fuel_tank: int, fuel_level: int):
        self.fuel_tank = fuel_tank
        self.fuel_type = fuel_type
        self.fuel_level = fuel_level

    def __add__(self, other):
        if isinstance(other, Gasoline) or isinstance(other, Diesel) or isinstance(other, Electric):
            if self. fuel_type == other.fuel_type:
                print(F"Transport refilled on {other.charge}")
                self.fuel_level = self.fuel_level + other.charge
                return self.fuel_level
        print("Transport needs another fuel type")
        return self.fuel_level

    @property
    def start_engine(self):
        if self.fuel_level > 0:
            print("Class print. Engine start: tank has {}".format(self.fuel_level))
            return True
        else:
            print("Something wrong")
            return False

    @start_engine.setter
    def start_engine(self, fuel_level: int):
        print("вызов __set_engine")
        self.fuel_level = fuel_level


class Engine:
    """Engine power, volume, fuel type(object one of Fuel class"""
    #__slots__ = ["power", "volume", "fuel", "turbine", "fuel_level"]

    def __init__(self, power: int, volume: int, turbine: bool = False, *args):
        self.power = power
        self.volume = volume
        self.turbine = turbine
        super().__init__(*args)

    @staticmethod
    def stop_engine():
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
        print(f"Your vehicle has {cls.wheels} wheels")

    def __eq__(self, other):
        if isinstance(other, Transport):
            return self.year == other.year

    def __contains__(self, item):
        if item in self.brand_db:
            print("brand in DB")
        else:
            self.brand_db.append(item)
            print("added brand in DB")


class Car(Transport, Engine, Tank):
    def __init__(self, body_type, *args):
        # sedan, suv, minivan ets.
        self.body_type = body_type
        super().__init__(*args)


class Bus(Transport, Engine, Tank):
    def __init__(self, seats_type, *args):
        # seats or sleeping bus
        self.seats_type = seats_type
        super().__init__(*args)


class Truck(Transport, Engine, Tank):

    wheels = 6

    max_carrying_capacity = 10000
    min_carrying_capacity = 3000

    def __init__(self, *args):
        super().__init__(*args)

    def set_carrying(self, carrying_capacity):
        if Truck.validate_carrying(carrying_capacity):
            self.carrying_capacity = carrying_capacity
            print(f"Class print. Truck has {self.carrying_capacity} carrying capacity")
            return self.carrying_capacity
        else:
            print("Wrong carrying capacity")

    @classmethod
    def validate_carrying(cls, arg):
        if cls.min_carrying_capacity <= arg <= cls.max_carrying_capacity:
            return True
        return False

    @classmethod
    def get_wheels(cls):
        print(f"Your vehicle has {cls.wheels} wheels")


class Bike(Transport, Engine, Tank):
    wheels = 2

    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def get_wheels(cls):
        print(f"Your vehicle has {cls.wheels} wheels")


if __name__ == "__main__":
    # charge
    gas_charge = Gasoline(35)
    diesel_charge = Diesel(50)
    # Tank fuel_type: str, fuel_tank: int, fuel_level: int
    car_tank = Tank("gas", 60, 0)
    truck_tank = Tank("diesel", 450, 0)

    # power: int, volume: int, turbine: bool = False
    car_eng = Engine(120, 2102)
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
    truck = Truck("renault", "red", 2011, 3, 560, 20750, True, "diesel", 450, 0)
    Truck.get_wheels()
    print("Carrying", truck.set_carrying(4500))
    print(truck + gas_charge)
    print(truck + diesel_charge)
    truck + diesel_charge
    truck.start_engine
    truck.start_engine = 30
    truck.start_engine

