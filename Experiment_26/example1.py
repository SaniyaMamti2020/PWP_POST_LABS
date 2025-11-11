import serial
import time

# --- Setup Serial Connection ---
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for Arduino to initialize

def send_command(command):
    """Send command to Arduino"""
    arduino.write(command.encode())
    print(f"Sent: {command}")

# --- Continuous Command Loop ---
while True:
    user_input = input("Enter '1' to turn ON LED, '0' to turn OFF, 'q' to quit: ").strip()
    
    if user_input in ['1', '0']:
        send_command(user_input)
    elif user_input.lower() == 'q':
        print("\nExiting...")
        print("3EK3_16_Saniya_Mamti")
        break
    else:
        print("Invalid input! Please enter '1', '0', or 'q'.")