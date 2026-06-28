import streamlit as st
import plotly.graph_objects as go
from src.battery import Battery
from src.soc import SOC
from src.soh import SOH
from src.protection import Protection
from src.balancing import CellBalancing

st.set_page_config(page_title="EV Battery Dashboard", layout="wide")

st.title("⚡ EV Battery Management System")
st.markdown("Real-time Battery Monitoring Dashboard")

# Sidebar inputs
st.sidebar.header("Battery Inputs")

voltage = st.sidebar.slider("Voltage (V)", 0.0, 60.0, 48.2)
current = st.sidebar.slider("Current (A)", 0.0, 20.0, 5.0)
temperature = st.sidebar.slider("Temperature (°C)", 0.0, 60.0, 30.0)
capacity = st.sidebar.slider("Capacity (Ah)", 0.0, 100.0, 50.0)

current_charge = st.sidebar.slider("Current Charge (Ah)", 0.0, 50.0, 35.0)
original_capacity = st.sidebar.slider("Original Capacity (Ah)", 0.0, 100.0, 50.0)

cell_voltages = [3.9, 4.0, 3.8, 4.1]

# Objects
battery = Battery(voltage, current, temperature, capacity)
soc = SOC(current_charge, capacity)
soh = SOH(capacity - 5, original_capacity)
protection = Protection(voltage, temperature)
balancer = CellBalancing(cell_voltages)

soc_value = soc.calculate_soc()
soh_value = soh.calculate_soh()

# Top metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Voltage", f"{voltage} V")
col2.metric("Current", f"{current} A")
col3.metric("SOC", f"{soc_value:.2f}%")
col4.metric("SOH", f"{soh_value:.2f}%")

if temperature > 45:
    st.warning(f"High Temperature: {temperature}°C")
else:
    st.info(f"Temperature: {temperature}°C")

# Safety status
status = protection.check_status()

if "Warning" in status:
    st.error(status)
else:
    st.success(status)

# Charts
st.subheader("Battery Performance")

fig = go.Figure()

fig.add_trace(go.Bar(
    x=["SOC", "SOH"],
    y=[soc_value, soh_value]
))

st.plotly_chart(fig, use_container_width=True)

# Cell balancing chart
st.subheader("Cell Voltage Balancing")
fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=soc_value,
    title={'text': "Battery Charge"},
    gauge={'axis': {'range': [0, 100]}}
))

st.plotly_chart(fig_gauge, use_container_width=True)
fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=[f"Cell {i+1}" for i in range(len(cell_voltages))],
    y=balancer.balance_cells()
))

st.plotly_chart(fig2, use_container_width=True)
st.subheader("Battery Summary")

if soh_value > 80:
    st.success("Battery health is good.")
elif soh_value > 60:
    st.warning("Battery health is moderate.")
else:
    st.error("Battery health is poor. Consider replacement.")