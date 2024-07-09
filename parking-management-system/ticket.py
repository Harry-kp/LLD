class Ticket:
    def __init__(self, parking_lot_no, floor_no, slot_no, vehicle):
        self.parking_lot_no = parking_lot_no
        self.floor_no = floor_no
        self.slot_no = slot_no
        self.vehicle = vehicle

    def __str__(self):
        return f'{self.parking_lot_no}_{self.floor_no}_{self.slot_no}'
    def __repr__(self):
        return f'{self.parking_lot_no}_{self.floor_no}_{self.slot_no}'
