class CellBalancing:
    def __init__(self, cell_voltages):
        self.cell_voltages = cell_voltages

    def balance_cells(self):
        avg_voltage = sum(self.cell_voltages) / len(self.cell_voltages)
        balanced = [round(avg_voltage, 2) for _ in self.cell_voltages]
        return balanced