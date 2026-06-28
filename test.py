from src.battery import Battery
from src.soc import SOC
from src.soh import SOH
from src.protection import Protection
from src.balancing import CellBalancing

battery = Battery(48.2, 5, 30, 50)
battery.display()

print()

soc = SOC(35, 50)
print(f"State of Charge (SOC): {soc.calculate_soc():.2f}%")

soh = SOH(45, 50)
print(f"State of Health (SOH): {soh.calculate_soh():.2f}%")

protection = Protection(48.2, 30)
print(protection.check_status())

cells = [3.9, 4.0, 3.8, 4.1]
balancer = CellBalancing(cells)
print("Balanced Cell Voltages:", balancer.balance_cells())