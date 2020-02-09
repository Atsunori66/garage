import sys
import tkinter as tk
import time

class mememe(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        master.title("foooooooo")

        self.canvas = tk.Canvas(master, width = 500, height = 500, bg = 'white')
        self.canvas.pack()

        self.canvas.create_oval(300 - 20, 300 - 20, 300 + 20, 300 + 20, fill = 'red', tag = 'circle1')
        self.canvas.create_oval(30, 30, 100, 100, fill = 'blue', tag = 'circle2')

        self.delay = 20
        self.auto_move()

        master.bind('<Up>', self.up)
        master.bind('<Down>', self.down)
        master.bind('<Left>', self.left)
        master.bind('<Right>', self.right)
        master.bind('<Escape>', self.escape)

    def up(self, event):
        self.canvas.move('circle1', 0, -10)

    def down(self, event):
        self.canvas.move('circle1', 0, 10)

    def left(self, event):
        self.canvas.move('circle1', -10, 0)

    def right(self, event):
        self.canvas.move('circle1', 10, 0)

    def escape(self, event):
        sys.exit()

    def auto_move(self):
        self.canvas.move('circle2', 0, 1)
        self.canvas.after(self.delay, self.auto_move)

def main():
    root = tk.Tk()
    app = mememe(master = root)
    app.mainloop()

if __name__ == "__main__":
    main()