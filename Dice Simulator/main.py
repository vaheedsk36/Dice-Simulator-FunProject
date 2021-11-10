from tkinter import *
import random
RANDOM_PINK = '#CF63A9'
OFF_WHITE = '#F8FAFF'
class Simulator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('310x310')
        self.window.resizable(0,0)
        self.window.title('Dice Simulator v0.1.0')
        self.window.config(bg=RANDOM_PINK)
        self.buttons()
        self.label()
        self.buttons_logic()
        

    def label(self):
        self.label = Label(self.window, font=("times",200),bg= RANDOM_PINK, fg= OFF_WHITE)

    def buttons_logic(self):
        self.numbers=['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.label.config(text = f'{random.choice(self.numbers)}')
        self.label.pack()
        return random.choice(self.numbers)

    def buttons(self):
        click = Button(self.window, text = "Simulate", 
        command = self.buttons_logic, padx= 30,pady= 10, bg = OFF_WHITE) 
        click.pack(side = RIGHT)   
        return click
    
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    simulator = Simulator()
    simulator.run()

