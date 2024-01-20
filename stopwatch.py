import tkinter as tk
import time
import threading

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ストップウォッチ")

        self.saved_time = self.load_saved_time()
        self.elapsed_time = 0.0
        self.running = False
        self.update_interval = 100  # 更新間隔 (ミリ秒)

        self.label = tk.Label(master, text=self.format_time(self.saved_time), font=("Helvetica", 60))
        self.label.pack(pady=30)

        self.start_button = tk.Button(master, text="スタート", bg="black", fg="white", width=20, command=self.start_stopwatch)
        self.start_button.pack(side=tk.LEFT, padx=20)
        
        self.stop_button = tk.Button(master, text="ストップ", bg="black", fg="white", width=20, command=self.stop_stopwatch)
        self.stop_button.pack(side=tk.LEFT, padx=20)
        self.stop_button["state"] = tk.DISABLED

        self.reset_button = tk.Button(master, text="リセット", bg="black", fg="white", command=self.reset_stopwatch)
        self.reset_button.pack(side=tk.LEFT, padx=20)
        self.reset_button["state"] = tk.NORMAL

        self.label.config(text=self.format_time(self.saved_time))
    
    def load_saved_time(self, filename="saved_time.txt"):
        try:
            with open(filename, "r") as file:
                saved_time_str = file.read().strip()
                return self.parse_time(saved_time_str)
        except FileNotFoundError:
            return 0

    def save_time(self, elapsed_time, filename="saved_time.txt"):
        with open(filename, "w") as file:
            file.write(self.format_time(elapsed_time))

    def start_stopwatch(self):
        if not self.running:
            if self.elapsed_time == 0.0:
                self.start_time = time.time() - self.saved_time
            else:
                self.start_time = time.time() - self.elapsed_time
                
            self.running = True
            self.start_button["state"] = tk.DISABLED
            self.stop_button["state"] = tk.NORMAL
            self.reset_button["state"] = tk.DISABLED
            self.update_display_threaded()

    def stop_stopwatch(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            self.start_button["state"] = tk.NORMAL
            self.stop_button["state"] = tk.DISABLED
            self.reset_button["state"] = tk.NORMAL
            self.save_time(self.elapsed_time)
            self.update_display()

    def reset_stopwatch(self):
        self.elapsed_time = 0.0
        self.running = False
        self.start_button["state"] = tk.NORMAL
        self.stop_button["state"] = tk.DISABLED
        self.reset_button["state"] = tk.DISABLED
        self.label.config(text=self.format_time(self.elapsed_time))
        self.start_time = time.time()
        self.save_time(0.0)
        
    def update_display_threaded(self):
        self.update_display()
        threading.Thread(target=self.update_elapsed_time).start()

    def update_elapsed_time(self):
        while self.running:
            self.elapsed_time = time.time() - self.start_time
            self.master.after(self.update_interval, self.update_display)

    def update_display(self):
        minutes, seconds = divmod(int(self.elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)
        time_str = f"{hours:04d}:{minutes:02d}:{seconds:02d}"
        self.label.config(text=time_str)

    def format_time(self, elapsed_time):
        hours, remainder = divmod(int(elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:04d}:{minutes:02d}:{seconds:02d}"

    def parse_time(self, time_str):
        try:
            hours, minutes, seconds = map(int, time_str.split(":"))
            return hours * 3600 + minutes * 60 + seconds
        except ValueError:
            return 0

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.geometry("500x300")
    root.configure(bg="white")
    root.mainloop()
