class SOH:
    def __init__(self, current_capacity, original_capacity):
        self.current_capacity = current_capacity
        self.original_capacity = original_capacity

    def calculate_soh(self):
        return (self.current_capacity / self.original_capacity) * 100