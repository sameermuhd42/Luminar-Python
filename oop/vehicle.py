class Vehicle:
    def vehicle_detail(self, manufacturer, model, color, reg_no):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.reg_no = reg_no
        print(self.manufacturer, self.model, self.color, self.reg_no)

    def __str__(self):
        return self.manufacturer


v1 = Vehicle()
v1.vehicle_detail("Ford", "Focus", "Blue", "KL07CR1111")
print(v1)
