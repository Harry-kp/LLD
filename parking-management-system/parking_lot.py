from ticket import Ticket
from vehicle import Vehicle

class ParkingLot:
    def __init__(self,no, no_of_floors, no_of_slots_per_floor):
        self.no = no
        self.layout = [['.' for j in range(no_of_slots_per_floor)] for i in range(no_of_floors)]
        self.tickets = dict()
        print(f'Created parking lot with {no_of_floors} floors and {no_of_slots_per_floor} slots per floor')

    @staticmethod
    def slot_type(slot_no):
        if slot_no == 0:
            return 'TRUCK'
        elif slot_no in (1,2):
            return 'BIKE'
        return 'CAR'

    def park(self, vehicle_type, color, registration_no):
        for floor_no, floor in enumerate(self.layout):
            for slot_no, slot in enumerate(floor):
                if self.slot_type(slot_no) == vehicle_type and not self.is_parked(floor_no,slot_no):
                    vehicle = Vehicle(vehicle_type,color,registration_no)
                    ticket = Ticket(self.no, floor_no+1, slot_no+1, vehicle)
                    self.tickets[str(ticket)] = ticket
                    self.layout[floor_no][slot_no] = 'X'
                    print(f'Parked vehicle. Ticket ID: {str(ticket)}')
                    return
        print('Parking Lot Full')

    def is_parked(self, floor_no, slot_no):
        return self.layout[floor_no][slot_no] == 'X'

    def unpark(self,ticket_id):
        if ticket_id in self.tickets:
            ticket = self.tickets[ticket_id]
            del self.tickets[ticket_id]
            self.layout[ticket.floor_no-1][ticket.slot_no-1] = '.'
            print(f'Unparked vehicle with Registration Number: {ticket.vehicle.registration_no} and Color: {ticket.vehicle.color}')
        else:
            print("Invalid Ticket")

    def free_count(self,vehicle_type):
        for floor_no, floor in enumerate(self.layout):
            cnt = 0
            for slot_no, slot in enumerate(floor):
                if  self.slot_type(slot_no) == vehicle_type and not self.is_parked(floor_no, slot_no):
                    cnt+=1
            print(f'No. of free slots for {vehicle_type} on Floor {floor_no+1}: {cnt}')


    def occupied_slots(self,vehicle_type):
        for floor_no, floor in enumerate(self.layout):
            occupied_slots = []
            for slot_no, slot in enumerate(floor):
                if  self.slot_type(slot_no) == vehicle_type and self.is_parked(floor_no, slot_no):
                    occupied_slots.append(slot_no+1)
            print(f'Occupied slots for {vehicle_type} on Floor {floor_no+1}: {','.join(map(str,occupied_slots))}')

    def free_slots(self,vehicle_type):
        for floor_no, floor in enumerate(self.layout):
            free_slots = []
            for slot_no, slot in enumerate(floor):
                if  self.slot_type(slot_no) == vehicle_type and not self.is_parked(floor_no, slot_no):
                    free_slots.append(slot_no+1)
            print(f'Free slots for {vehicle_type} on Floor {floor_no+1}: {','.join(map(str,free_slots))}')
