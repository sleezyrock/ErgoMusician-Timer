import time
import threading
import random
from plyer import notification

STRETCHING_TIPS = [
    "Wrist Flexor Stretch: Extend your arm with your palm facing up. Use your other hand to gently press your fingers down towards the floor.",
    "Wrist Extensor Stretch: Extend your arm with your palm facing down. Use your other hand to gently press your fingers towards your body.",
    "Neck Stretch: Gently tilt your head to one side, bringing your ear toward your shoulder. Hold for 15 seconds.",
    "Shoulder Roll: Roll your shoulders forward in a circular motion, then backward.",
    "Finger Spread: Spread your fingers as far apart as possible, hold for 5 seconds, and release.",
    "Thumb Stretch: Pull your thumb gently towards your wrist to stretch the base.",
    "Posture Check: Sit up straight, align your ears over your shoulders, and relax your back."
]

def metronome(bpm):
    interval = 60.0 / bpm
    print(f"Starting metronome at {bpm} BPM. Press Ctrl+C to stop.")
    try:
        while True:
            # Simple visual metronome
            print("Tick", end="\r", flush=True)
            time.sleep(interval / 2)
            print("Tock", end="\r", flush=True)
            time.sleep(interval / 2)
    except KeyboardInterrupt:
        print("\nMetronome stopped.")

def ergonomic_timer(interval_minutes):
    interval_seconds = interval_minutes * 60
    while True:
        time.sleep(interval_seconds)
        tip = random.choice(STRETCHING_TIPS)
        try:
            notification.notify(
                title="Musician's Ergonomic Timer",
                message=tip,
                app_name="ErgoMusician-Timer",
                timeout=10
            )
        except Exception as e:
            print(f"\n[Notification] {tip}")

def main():
    print("--- Musician's Ergonomic Timer ---")

    # Allow user to input BPM
    try:
        bpm_input = input("Enter BPM for metronome (default 60): ")
        bpm = int(bpm_input) if bpm_input.strip() else 60
    except ValueError:
        print("Invalid input, defaulting to 60 BPM.")
        bpm = 60

    interval_minutes = 20
    print(f"Ergonomic timer started. You will be notified every {interval_minutes} minutes to stretch.")

    # Start the background timer thread
    timer_thread = threading.Thread(target=ergonomic_timer, args=(interval_minutes,), daemon=True)
    timer_thread.start()

    # Start the metronome in the main thread
    metronome(bpm)

if __name__ == "__main__":
    main()
