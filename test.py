from pyW215.pyW215 import SmartPlug, ON, OFF
from time import sleep

sp = SmartPlug('192.168.1.155', '397381')

# Get values if available otherwise return N/A
print(sp.current_consumption)
print(sp.temperature)
print(sp.total_consumption)

# Check the current state
current_state = sp.state
print(f"Current switch state: {current_state}")

# Turn switch on and off
if current_state == ON:
    sp.state = OFF
    print("Switch is ON, turning OFF...")
else:
    sp.state = ON
    print("Switch is OFF, turning ON...")

# Check the state after attempting to change it
sleep(5)  # Warten, um die Änderung abzuwarten
new_state = sp.state
print(f"Switch state after operation: {new_state}")