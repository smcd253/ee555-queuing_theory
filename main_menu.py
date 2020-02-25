from tkinter import Tk, Label, Button, END, W, E
import math         # factorial

# add children directories to path so we can
# import main menu
import sys
sys.path.insert(1, 'p1-erlang_b/') 
class MainMenu:

    def __init__(self):
        self.root = Tk()
        self.root.title("EE555 Mini Project - Main Menu")

        # menu option buttons
        self.erlang_b = Button(self.root, text="Erlang-B", command=lambda: self.update("Erlang-B"))

        # menu Layout
        self.erlang_b.grid(row=3, column=0)

    def update(self, method):
        if method == "Erlang-B":
            self.root.destroy()
            from erlang_b_gui import ErlangB
            erlang_menu = ErlangB()
            erlang_menu.root.mainloop()

def main():
    m_menu = MainMenu()
    m_menu.root.mainloop()

if __name__ == '__main__':
    main()