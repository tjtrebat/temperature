__author__ = 'Tom'

from Tkinter import *

class Temperature:
    def __init__(self, root):
        self.root = root
        self.fahrenheit = DoubleVar()
        self.celsius = DoubleVar()
        self.add_temperature("Fahrenheit", self.fahrenheit)
        self.add_temperature("Celsius", self.celsius)
        self.add_buttons()

    def add_temperature(self, text, var):
        frame = Frame(self.root)
        frame.pack()
        Label(frame, text=text).pack(side=LEFT)
        Entry(frame, textvariable=var).pack(side=RIGHT)

    def add_buttons(self):
        frame = Frame(self.root)
        frame.pack()
        Button(frame, text="Convert", command=self.convert).pack(side=LEFT)
        Button(frame, text="Clear", command=self.clear).pack(side=RIGHT)

    def convert(self):
        celsius = self.get_temperature(self.celsius)
        fahrenheit = self.get_temperature(self.fahrenheit)
        if celsius == 0: # convert fahrenheit to celsius
            self.celsius.set((5.0 / 9) * (fahrenheit - 32))
        elif fahrenheit == 0: # convert celsius to fahrenheit
            self.fahrenheit.set((9.0 / 5) * (celsius + 32))

    def get_temperature(self, temp):
        try:
            return temp.get()
        except ValueError:
            return float()

    def clear(self):
        self.fahrenheit.set(0.0)
        self.celsius.set(0.0)

if __name__ == "__main__":
    root = Tk()
    Temperature(root)
    root.mainloop()
  