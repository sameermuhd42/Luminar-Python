class Vehicle:
    def vehicle_detail(self, manufacturer, model, color, reg_no):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.reg_no = reg_no
        print(self.manufacturer, self.model, self.color, self.reg_no)


class Bus(Vehicle):
    def bus_detail(self, seats, deck):
        self.seats = seats
        self.deck = deck
        print(self.seats, self.deck)


b1 = Bus()
b1.vehicle_detail("Scania", "Citywide", "Black", "KL07CR1111")
b1.bus_detail(60, "Single")
