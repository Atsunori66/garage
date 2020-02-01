import sys
import tkinter as tk

class mememe(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        master.title("foooooooo")

        self.canvas = tk.Canvas(master, width = 500, height = 500, bg = 'white')
        self.canvas.pack()

        self.canvas.create_oval(5, 5, 40, 40, fill = 'red', tag = 'circle1')

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

def main():
    root = tk.Tk()
    app = mememe(master = root)
    app.mainloop()

if __name__ == "__main__":
    main()