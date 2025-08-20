'''
This is an unwanted file, just for testing
'''
from PeriodicTimer import TimerIRQ

def periodic_task():
    print(f"Triggered")

# Create a periodic timer that triggers every 2 seconds
periodic_timer = TimerIRQ(1, periodic_task)
periodic_timer.start()

print("Periodic timer started. Press Ctrl+C to stop.")

try:
    while True:
        pass
except KeyboardInterrupt:
    periodic_timer.stop()
    print("\nPeriodic timer stopped.")