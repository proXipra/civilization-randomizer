import tkinter
from tkinter import *
import random


class SidsMixer(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mixer v2.5")
        self.geometry("265x260")
        self.count = 0
        self.dict1 = {}
        self.dict2 = {}
        self.entryVariable = tkinter.StringVar()

        self.MainEntry = tkinter.Entry(self, textvariable=self.entryVariable,
                                       bd=3, width=12, font=('Times New Roman', 12))
        self.MainEntry.place(x=60, y=10)
        self.MainEntry.bind("<Return>", self.EventHandler)

        self.ButtonEnter = Button(self, command=self.LabelCreator, text='Enter', font=('Helvetica', 10), bg='yellow')
        self.ButtonEnter.place(x=170, y=8)

        self.ButtonDel = Button(self, text='Del', command=self.Delete,
                                height=1, font=('Helvetica', 10), bg='red', width=3)
        self.ButtonDel.place(x=20, y=8)

        self.ButtonGo = Button(self, text='GO', command=self.EntryCreator, height=1, font=('Helvetica', 10), bg='green')
        self.ButtonGo.place(x=215, y=8)

        self.ButtonCiv = Button(self, text="Ülke", command=lambda: [self.Set_Players()], height=1, width=5)
        self.ButtonCiv.place(x=85, y=215)

        self.EntryMap = tkinter.Entry(self, width=17, font=('Italic', 10), relief=SUNKEN, justify='center')
        self.EntryMap.place(x=70, y=180)

        self.ButtonMap = Button(self, text="Harita", command=lambda: self.set_map(), height=1, width=5)
        self.ButtonMap.place(x=135, y=215)

        self.leaders = ["Ahmad al-Mansur", "Alexander", "Ashurbanipal", "Askia", "Attila",
                        "Augustus Caesar", "Bismarck", "Boudicca", "Casimir III", "Catherine",
                        "Darius I", "Dido", "Elizabeth", "Enrico Dandolo", "Gajah Mada", "Gandhi",
                        "Genghis Khan", "Gustavus Adolphus", "Haile Selassie", "Harald Bluetooth",
                        "Harun al-Rashid", "Hiawatha", "Isabella", "Kamehameha", "Maria I",
                        "Maria Theresa", "Montezuma", "Napoleon", "Nebuchadnezzar II",
                        "Oda Nobunaga", "Pacal(Maya)", "Pachacuti(Inca)", "Pedro II", "Pocatello",
                        "Ramesses II", "Ramkhamhaeng(Siam)", "Sejong(Korea)", "Shaka", "Suleiman",
                        "Theodora", "Washington", "William", "Wu Zetian"]

        self.maps = ["Pangea", "Continents", "Earth", "Small Continents", "Fractal", "Okyanusya", "Archipelago"]

    def EventHandler(self, event):
        self.LabelCreator()

    def LabelCreator(self):  # This method creates label and entry as dict item! But just places the label.
        main_entry = self.entryVariable.get()
        if len(main_entry.strip()) != 0:
            self.dict1[self.count] = tkinter.Label(self, text=main_entry, font=('Times New Roman', 11))
            self.dict1[self.count].place(x=15, y=50+(self.count*20))
            self.count += 1
            self.MainEntry.delete(0, END)
        else:
            print('Empty Entry!')
        print(self.dict1)
        print(self.dict2)

    def EntryCreator(self):
        if len(self.dict2) != 0:
            x = len(self.dict2.keys())
            y = len(self.dict1.keys())
        else:
            x = 0
            y = len(self.dict1.keys())
        print(self.dict2)
        for i in range(x, y):
            print("hhh")
            self.dict2[i] = Entry(self, relief=GROOVE, justify='center', font=("Cambria", 11))
            self.dict2[i].place(x=85, y=50 + (i * 20))

    def Delete(self):
        if len(self.dict1) == len(self.dict2):
            self.dict1.get(max(self.dict1.keys())).place_forget()
            self.dict1.popitem()
            self.dict2.get(max(self.dict2.keys())).place_forget()
            self.dict2.popitem()
        elif len(self.dict1) > len(self.dict2):

            self.dict1.get(max(self.dict1.keys())).place_forget()
            self.dict1.popitem()
        else:
            print("Something goes wrong!")
        if self.count != 0:
            self.count -= 1
        print(self.dict1)
        print(self.dict2)
        print(self.count)

    def Set_Players(self):
        for i in self.dict2.values():
            i.delete(0, END)
        copy = self.leaders.copy()
        random.shuffle(copy)
        for i in self.dict2.values():
            i.insert(0, copy.pop())

    def set_map(self):
        self.EntryMap.delete(0, END)
        copy = self.maps.copy()
        random.shuffle(copy)
        self.EntryMap.insert(0, copy.pop())


if __name__ == "__main__":
    app = SidsMixer()
    app.mainloop()
