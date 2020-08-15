import random
import tkinter as tk


def read_data():
        data = []
        f = open('data/wild_magic.txt', 'r', encoding= 'utf-8')
        for line in f:
            data.append(line)
        f.close()
        return data

class Application(tk.Frame):
    magic = []
    def __init__(self, master= None):
        super().__init__(master)
        self.master = master
        self.magic = read_data()
        self.pack()
        self.create_widgets()
        
    
    def create_widgets(self):
        self.lab = tk.Label(self, text= 'Output will be displayed here')
        self.lab.pack(side= 'top')
        self.roll = tk.Button(self)
        self.roll['text'] = 'ROLL'
        self.roll['command'] = self.get_effect
        self.roll.pack(side= 'left')
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side= 'bottom')

    def get_effect(self):
        r = random.randint(0, len(self.magic) - 1)
        self.lab['text'] = self.magic[r]


def main():
    root = tk.Tk()
    app = Application(master= root)
    app.mainloop()
    
    

if __name__ == '__main__':
    main()