import tkinter as tk
import time


class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        self.work_sec = 25 * 60  # 25 minutes for work
        self.break_sec = 5 * 60  # 5 minutes for break
        self.time_left = self.work_sec
        self.is_break = False
        self.running = False

        self.time_label = tk.Label(master, text=self.format_time(self.work_sec))
        self.time_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack()

        self.update_timer()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def reset_timer(self):
        self.running = False
        self.is_break
    def reset_timer(self):
        self.running = False
        self.is_break = False
        self.time_left = self.work_sec
        self.update_timer()

    def update_timer(self):
        if self.running:
            if self.time_left > 0:
                self.time_label.config(text=self.format_time(self.time_left))
                self.time_left -= 1
                self.master.after(1000, self.update_timer)
            else:
                self.running = False
                self.is_break = not self.is_break
                if self.is_break:
                    self.time_left = self.break_sec
                else:
                    self.time_left = self.work_sec
                self.update_timer()

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds %= 60
        return f"{minutes:02d}:{seconds:02d}"

def main():
    root = tk.Tk()
    timer = PomodoroTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
