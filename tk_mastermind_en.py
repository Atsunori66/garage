import random
import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.geometry("800x500")
        self.master.title('Mastermind')

        self.master.bind('<Escape>', self.close)
        self.master.bind('<Return>', self.mastermind)

        self.widget()
        self.life = 10

        self.list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.master_numbers = random.sample(self.list, 4)

    def widget(self):
        self.intro = tk.Label(self.master, text=' Guess my number; 4-digit, non-duplicates ', font=('MS Gothic', 12))
        self.intro.grid(row=1, column=1)
        self.box = tk.Entry(self.master, width=25)
        self.box.grid(row=1, column=2)
        self.box.focus_set()
        self.note = tk.Label(self.master, text=' Enter to try, Esc to quit', font=('MS Gothic', 10))
        self.note.grid(row=1, column=3)

    def close(self, event):
        self.master.destroy()

    def mastermind(self, event):
        self.hit = 0
        self.blow = 0

        while True:
            self.guess = self.box.get()

            if self.guess.isnumeric() == False:
                self.info = tk.messagebox.showinfo('', 'Number please!')
                self.box.delete(0, tk.END)
                break

            elif len(self.guess) < 4:
                self.info = tk.messagebox.showinfo('', 'Too short!')
                self.box.delete(0, tk.END)
                break

            elif len(self.guess) > 4:
                self.info = tk.messagebox.showinfo('', 'Too long!')
                self.box.delete(0, tk.END)
                break

            elif len(self.guess) != len(set(self.guess)):
                self.info = tk.messagebox.showinfo('', 'Dupe!')
                self.box.delete(0, tk.END)
                break

            elif len(self.guess) == len(set(self.guess)):
                if self.guess[0] in self.master_numbers:
                    if self.guess[0] == self.master_numbers[0]:
                        self.hit += 1
                    else:
                        self.blow += 1

                if self.guess[1] in self.master_numbers:
                    if self.guess[1] == self.master_numbers[1]:
                        self.hit += 1
                    else:
                        self.blow += 1

                if self.guess[2] in self.master_numbers:
                    if self.guess[2] == self.master_numbers[2]:
                        self.hit += 1
                    else:
                        self.blow += 1

                if self.guess[3] in self.master_numbers:
                    if self.guess[3] == self.master_numbers[3]:
                        self.hit += 1
                    else:
                        self.blow += 1

                if self.hit == 4:
                    self.info = tk.messagebox.showinfo('', 'You got it!')
                    self.box.delete(0, tk.END)
                    break

                if self.life == 0:
                    self.info = tk.messagebox.showinfo('Game over!', 'Master: ' + self.master_numbers[0] + self.master_numbers[1] + self.master_numbers[2] + self.master_numbers[3])
                    self.box.delete(0, tk.END)
                    break

                if self.hit < 4:
                    self.you_guessed = tk.Label(self.master, text='You guessed: ' + str(self.guess), font=('MS Gothic', 12), fg='#007fff')
                    self.you_guessed.grid(row=14 - self.life, column=1)
                    self.hit_blow = tk.Label(self.master, text='Hit: ' + str(self.hit) + ', ' + 'Blow: ' + str(self.blow), font=('MS Gothic', 12))
                    self.hit_blow.grid(row=14 - self.life, column=2)
                    self.life_left = tk.Label(self.master, text='Life left: ' + str(self.life), font=('MS Gothic', 12), fg='#e34234')
                    self.life_left.grid(row=14 - self.life, column=3)
                    self.box.delete(0, tk.END)
                    self.life -= 1
                    break

            self.hit = 0
            self.blow = 0

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()