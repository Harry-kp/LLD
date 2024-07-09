from parking_lot import ParkingLot
import parking_lot

parkinglot = None

while True:
    instruction = input()
    if instruction == 'exit':
        break

    commands = instruction.split(' ')
    if commands[0] == 'create_parking_lot':
        parkinglot = ParkingLot(commands[1],int(commands[2]),int(commands[3]))
    elif commands[0] == 'display':
        if commands[1] == 'free_count':
            parkinglot.free_count(commands[2])
        elif commands[1] == 'free_slots':
            parkinglot.free_slots(commands[2])
        elif commands[1] == 'occupied_slots':
            parkinglot.occupied_slots(commands[2])
    elif commands[0] == 'park_vehicle':
        parkinglot.park(commands[1],commands[3],commands[2])
    elif commands[0] == 'unpark_vehicle':
        parkinglot.unpark(commands[1])
