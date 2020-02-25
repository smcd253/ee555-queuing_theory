from tkinter import Tk, Label, Button, END, W, E
import math         # factorial

# add children directories to path so we can
# import main menu
import sys
sys.path.insert(1, 'p1-erlang_b/') 
sys.path.insert(1, 'p2-erlang_c/') 
sys.path.insert(1, 'p3-cyclic/') 


class MainMenu:

    def __init__(self):
        self.root = Tk()
        self.root.title("EE555 Mini Project - Main Menu")

        # menu option buttons
        self.erlang_b = Button(self.root, text="Erlang-B", command=lambda: self.update("Erlang-B"))
        self.erlang_c = Button(self.root, text="Erlang-C", command=lambda: self.update("Erlang-C"))
        self.cylcic = Button(self.root, text="Cyclic", command=lambda: self.update("Cyclic"))

        # menu Layout
        self.erlang_b.grid(row=3, column=0)
        self.erlang_c.grid(row=3, column=1)
        self.cylcic.grid(row=3, column=2)

    def update(self, method):
        if method == "Erlang-B":
            self.root.destroy()
            from erlang_b_gui import ErlangB
            erlang_menu = ErlangB()
            erlang_menu.root.mainloop()

        elif method == "Erlang-C":
            self.root.destroy()
            from erlang_c_gui import ErlangC
            erlang_c_menu = ErlangC()
            erlang_c_menu.root.mainloop()

        elif method == "Cyclic":
            self.root.destroy()
            from cyclic_gui import Cyclic
            cyclic_menu = Cyclic()
            cyclic_menu.root.mainloop()

def main():
    m_menu = MainMenu()
    m_menu.root.mainloop()

if __name__ == '__main__':
    main()