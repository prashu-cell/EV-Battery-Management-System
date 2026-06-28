class Battery:
    def __init__(self, voltage, current, temperature, capacity):
        self.voltage = voltage
        self.current = current
        self.temperature = temperature
        self.capacity = capacity

    def display(self):
        print("Battery Information")
        print("-------------------")
        print(f"Voltage      : {self.voltage} V")
        print(f"Current      : {self.current} A")
        print(f"Temperature  : {self.temperature} °C")
        print(f"Capacity     : {self.capacity} Ah")