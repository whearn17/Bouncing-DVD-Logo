import random
import tkinter as tk
import time


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.overrideredirect(True)

        self.dvd_logo = tk.PhotoImage(file="dvd_logo.png")
        self.label = tk.Label(self, image=self.dvd_logo, bg="white")

        self.wm_attributes("-transparentcolor", "white")

        self.label.pack()

        self.x = random.randint(0, 1920)
        self.y = random.randint(0, 1080)

        self.speedx = 3
        self.speedy = 3

        self.bind('<KeyPress>', self.on_key_press)

        self.lock = 0

    def check_collisions(self):
        if self.x > 1920 - 252:
            self.speedx = -3
        if self.x < 0:
            self.speedx = 3
        if self.y > 1080 - 115:
            self.speedy = -3
        if self.y < 0:
            self.speedy = 3

    def update_position(self):
        self.x += self.speedx
        self.y += self.speedy
        self.geometry("+" + str(self.x) + "+" + str(self.y))

    def on_key_press(self, event):
        while self.lock:
            pass
        self.lock = 1
        if event.char == "k" and event.state == 131080:
            self.destroy()
        self.lock = 0


if __name__ == "__main__":
    window = Window()
    while not window.lock:
        window.lock = 1
        window.check_collisions()
        window.update_position()
        window.lock = 0
        window.update()
        time.sleep(1./60)
    window.mainloop()
