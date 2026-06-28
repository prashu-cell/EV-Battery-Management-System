class SOC:
    def __init__(self, current_charge, max_capacity):
        self.current_charge = current_charge
        self.max_capacity = max_capacity

    def calculate_soc(self):
        return (self.current_charge / self.max_capacity) * 100