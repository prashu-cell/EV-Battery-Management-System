class Protection:
    def __init__(self, voltage, temperature):
        self.voltage = voltage
        self.temperature = temperature

    def check_status(self):
        if self.voltage > 54:
            return "Warning: Overvoltage detected!"
        elif self.temperature > 45:
            return "Warning: Overheating detected!"
        else:
            return "Battery operating safely."