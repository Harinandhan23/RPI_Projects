import serial
import time

# Configure the serial port
# Use '/dev/serial0' for the primary UART
# Or '/dev/ttyS0' or '/dev/ttyAMA0' depending on your Raspberry Pi model and configuration
# Baud rate must match the device you are communicating with
ser = serial.Serial(
    port='/dev/ttyS0',  # Replace with your serial port
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    rtscts = 0,
    timeout=1 # Timeout in seconds for read operations
)

print(f"Serial port opened: {ser.name}")

try:
    while True:
        # Sending data
        send_data = "Hello from Raspberry Pi!\n"
        ser.write(send_data.encode()) # Encode string to bytes
        print(f"Sent: {send_data.strip()}")

        # Receiving data
        if ser.in_waiting > 0:
            received_data = ser.readline().decode().strip() # Read line and decode bytes to string
            print(f"Received: {received_data}")

        time.sleep(2) # Wait for 2 seconds before sending/receiving again

except KeyboardInterrupt:
    print("\nExiting program.")
finally:
    ser.close()
    print("Serial port closed.")