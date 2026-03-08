import time
import threading
import random
import tkinter as tk
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

class ErgonomicTimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Musician's Ergonomic Timer")
        self.root.geometry("400x300")

        self.bpm = tk.IntVar(value=60)
        self.is_running = False
        self.tick_state = False

        self._setup_ui()
        self._start_ergonomic_timer()

    def _setup_ui(self):
        # Title Label
        title_label = tk.Label(self.root, text="ErgoMetronome", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Visual Metronome Indicator
        self.indicator = tk.Canvas(self.root, width=50, height=50, bg="grey")
        self.indicator_oval = self.indicator.create_oval(5, 5, 45, 45, fill="white")
        self.indicator.pack(pady=10)

        # BPM Display
        self.bpm_label = tk.Label(self.root, text=f"BPM: {self.bpm.get()}", font=("Helvetica", 14))
        self.bpm_label.pack(pady=5)

        # BPM Slider (40 to 200)
        self.bpm_slider = tk.Scale(
            self.root,
            from_=40,
            to=200,
            orient=tk.HORIZONTAL,
            variable=self.bpm,
            command=self._update_bpm_label,
            length=250
        )
        self.bpm_slider.pack(pady=10)

        # Start/Stop Button
        self.start_stop_btn = tk.Button(
            self.root,
            text="Start Metronome",
            font=("Helvetica", 12),
            command=self._toggle_metronome,
            width=15
        )
        self.start_stop_btn.pack(pady=10)

    def _update_bpm_label(self, event=None):
        self.bpm_label.config(text=f"BPM: {self.bpm.get()}")

    def _toggle_metronome(self):
        if self.is_running:
            self.is_running = False
            self.start_stop_btn.config(text="Start Metronome")
            self.indicator.itemconfig(self.indicator_oval, fill="white")
        else:
            self.is_running = True
            self.start_stop_btn.config(text="Stop Metronome")
            self._tick()

    def _tick(self):
        if not self.is_running:
            return

        bpm_val = self.bpm.get()
        if bpm_val <= 0:
            bpm_val = 60

        # Time for a single beat in ms
        interval_ms = int((60.0 / bpm_val) * 1000)

        # Toggle indicator color for visual tick
        if self.tick_state:
            self.indicator.itemconfig(self.indicator_oval, fill="green")
        else:
            self.indicator.itemconfig(self.indicator_oval, fill="blue")

        self.tick_state = not self.tick_state

        # Schedule next tick
        self.root.after(interval_ms, self._tick)

    def _start_ergonomic_timer(self):
        interval_minutes = 20
        timer_thread = threading.Thread(target=self._ergonomic_timer_loop, args=(interval_minutes,), daemon=True)
        timer_thread.start()

    def _ergonomic_timer_loop(self, interval_minutes):
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
    root = tk.Tk()
    app = ErgonomicTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
