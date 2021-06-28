import random
from enum import Enum
from abc import ABC, abstractmethod


class CannotReceiveEquipmentException(Exception):
    pass


class EquipmentType(Enum):
    PRINTER = 0
    SCANNER = 1
    XEROX = 2

    def __str__(self):
        return self.name


class OfficeEquipmentWarehouse:

    def __init__(self, size, temperature):
        self.size = size
        self.temperature = temperature
        self.equipment_storage = {
            EquipmentType.PRINTER: [],
            EquipmentType.SCANNER: [],
            EquipmentType.XEROX: []
        }

    @staticmethod
    def validate_equipment(equipment, number, warehouse_temp, warehouse_space):
        if type(number) is not int:
            raise ValueError(f"Cannot parse number of equipment, it should be a {int}, but was {type(number)}")
        if equipment.min_storage_temperature > warehouse_temp:
            raise CannotReceiveEquipmentException(f"This warehouse is too cold({warehouse_temp}) for {equipment}")
        if warehouse_space - number < 0:
            raise CannotReceiveEquipmentException(
                f"This warehouse has no space to receive {number} {equipment}. Storage left: {warehouse_space}")

    count = 0

    def store_equipment(self, equipment):
        self.count += 1
        print(f"Storing #{self.count} {equipment}")
        if type(equipment) is Printer:
            self.equipment_storage[EquipmentType.PRINTER].append(equipment)
        elif type(equipment) is Scanner:
            self.equipment_storage[EquipmentType.SCANNER].append(equipment)
        elif type(equipment) is Xerox:
            self.equipment_storage[EquipmentType.XEROX].append(equipment)
        self.size -= 1

    def receive_equipment(self, equipment_list, number):
        self.count = 0
        for equipment in equipment_list:
            try:
                if OfficeEquipment in type(equipment).mro():
                    self.validate_equipment(equipment, number, self.temperature, self.size)
                    self.store_equipment(equipment)
                else:
                    raise ValueError(
                        f"Warehouse cannot store {type(equipment)} OfficeEquipment.mro{OfficeEquipment.mro()}")
            except ValueError as err:
                print(err)
            except CannotReceiveEquipmentException as err:
                print(err)

    def storage_state(self):
        number_of_printers = len(self.equipment_storage[EquipmentType.PRINTER])
        number_of_scanners = len(self.equipment_storage[EquipmentType.SCANNER])
        number_of_xeroxes = len(self.equipment_storage[EquipmentType.XEROX])
        print(
            f"Storage contains {number_of_printers} printers {number_of_scanners} scanners and {number_of_xeroxes} xeroxes")
        print(f"Space left = {self.size}")

    def send_equipment(self, equipment_type, number, destination):
        for i in range(0, number):
            self.equipment_storage[equipment_type].pop()
            self.size += 1
        print(f"Sending {number} {equipment_type} to {destination} space left: {self.size}")


class OfficeEquipment(ABC):
    def __init__(self, serial_number, min_storage_temperature, state):
        self.serial_number = serial_number
        self.min_storage_temperature = min_storage_temperature
        self.state = state

    @abstractmethod
    def turn_on(self):
        self.state = "ON"
        pass

    @abstractmethod
    def turn_off(self):
        self.state = "OFF"
        pass

    def __str__(self):
        return f"{type(self).__name__}: {vars(self)}"


class Printer(OfficeEquipment):

    def __init__(self, print_capacity, serial_number, min_storage_temperature, state):
        super().__init__(serial_number, min_storage_temperature, state)
        self.print_capacity = print_capacity

    def turn_on(self):
        print(f"Printer turned {self.state}")

    def turn_off(self):
        print(f"Printer turned {self.state}")


class Scanner(OfficeEquipment):

    def __init__(self, is_double_sided, serial_number, min_storage_temperature, state):
        super().__init__(serial_number, min_storage_temperature, state)
        self.is_double_sided = is_double_sided

    def turn_on(self):
        print(f"Scanner turned {self.state}")

    def turn_off(self):
        print(f"Scanner turned {self.state}")


class Xerox(OfficeEquipment):

    def __init__(self, capacity, speed, is_double_sided, serial_number, min_storage_temperature, state):
        super().__init__(serial_number, min_storage_temperature, state)
        self.capacity = capacity
        self.speed = speed
        self.is_double_sided = is_double_sided

    def turn_on(self):
        print(f"Xerox turned {self.state}")

    def turn_off(self):
        print(f"Xerox turned {self.state}")


cold_warehouse = OfficeEquipmentWarehouse(200, 5)
warm_warehouse = OfficeEquipmentWarehouse(300, 15)

printers = [
    Printer(
        min_storage_temperature=14,
        print_capacity=200,
        serial_number=random.randint(0, 1000),
        state="OFF"
    )
    for i in range(0, 350)
]
scanners = [
    Scanner(
        min_storage_temperature=4,
        is_double_sided=False,
        serial_number=random.randint(0, 1000),
        state="OFF"
    )
    for j in range(0, 350)
]

xeroxes = [
    Xerox(
        min_storage_temperature=4,
        is_double_sided=False,
        serial_number=random.randint(0, 1000),
        state="OFF",
        capacity=250,
        speed=20
    )
    for n in range(0, 350)
]

cold_warehouse.receive_equipment(printers[0:50], 1)
warm_warehouse.receive_equipment(printers[0:50], 50)
warm_warehouse.storage_state()
warm_warehouse.send_equipment(EquipmentType.PRINTER, 24, "Mail.Group")
