import sys, random
import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.geometry("600x600")
        self.master.title('Mastermind')
        self.widget()
        self.master.bind('<Escape>', self.close)
        self.master.bind('<Return>', self.mastermind)

        self.list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.master_numbers = random.sample(self.list, 4)
        self.life = 10

    def widget(self):
        self.intro = tk.Label(self.master, text = '重複なしで4ケタの数字を入れてね', font = ('メイリオ', 12))
        self.intro.place(x = 200, y = 40)

        self.explanation = tk.Label(self.master, text = 'Enter で入力, Esc で終了', font = ('メイリオ', 8))
        self.explanation.place(x = 200, y = 70)

        self.box = tk.Entry(self.master, width = 20)
        self.box.place(x = 200, y = 100)
        self.box.focus_set()

    def close(self, event):
        self.master.destroy()

    def mastermind(self, event):
        self.hit = 0
        self.blow = 0
        
        while True:
            self.guess = self.box.get()

            if self.guess.isnumeric() == False:
                self.info = tk.messagebox.showinfo('注意', '数字を!')
                self.box.delete(0, tk.END)
                break

            elif len(self.guess) < 4:
                self.info = tk.messagebox.showinfo('注意', '足らん!')
                self.box.delete(0, tk.END)
                break

            elif len(self.guess) > 4:
                self.info = tk.messagebox.showinfo('注意', '多い!')
                self.box.delete(0, tk.END)
                break

            elif len(self.guess) != len(set(self.guess)):
                self.info = tk.messagebox.showinfo('注意', '重複!')
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
                    self.congrats = tk.messagebox.showinfo('', '見事!')
                    self.box.delete(0, tk.END)
                    break

                if self.life == 0:
                    self.fail = tk.Label(self.master, text = '残念!', font = ('メイリオ', 12))
                    self.fail.place(x = 200, y = 250)
                    self.show_master = tk.Label(self.master, text = 'Master: ' + self.master_numbers[0] + self.master_numbers[1] + self.master_numbers[2] + self.master_numbers[3], font = ('Cascadia Code', 12))                    
                    self.show_master.place(x = 200, y = 280)
                    self.box.delete(0, tk.END)
                    break

                if self.hit < 4: 
                    self.your_hand = tk.Label(self.master, text = 'Your hand: ' + str(self.guess), font = ('Cascadia Code', 12))
                    self.your_hand.place(x = 200, y = 130)
                    self.hit_blow = tk.Label(self.master, text = 'Hit: ' + str(self.hit) + ', ' + 'Blow: ' + str(self.blow), font = ('Cascadia Code', 12))
                    self.hit_blow.place(x = 200, y = 170)
                    self.life_left = tk.Label(self.master, text = 'Life left: ' + str(self.life), font = ('Cascadia Code', 12))
                    self.life_left.place(x = 200, y = 210)
                    '''
                    self.show_master = tk.Label(self.master, text = 'master: ' + self.master_numbers[0] + ', ' + self.master_numbers[1]+ ', ' + self.master_numbers[2] + ', ' + self.master_numbers[3])                    
                    self.show_master.place(x = 200, y = 250)
                    '''
                    self.box.delete(0, tk.END)
                    self.life -= 1
                    break

            self.hit = 0
            self.blow = 0

def main():
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()

if __name__ == "__main__":
    main()