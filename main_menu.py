from tkinter import Tk, Label, Button, END, W, E
import math         # factorial

# add children directories to path so we can
# import main menu
import sys
sys.path.insert(1, 'src/p1-erlang_b/') 
sys.path.insert(1, 'src/p2-erlang_c/') 
sys.path.insert(1, 'src/p3-cyclic/') 
sys.path.insert(1, 'src/p4-mm1k/') 
sys.path.insert(1, 'src/p5-two_servers/') 

class MainMenu:

    def __init__(self, f_path):
        self.root = Tk()
        self.root.title("EE555 Mini Project - Main Menu")

        # excel path
        self.f_path = f_path

        # menu option buttons
        self.erlang_b = Button(self.root, text="Erlang-B", command=lambda: self.update("Erlang-B"))
        self.erlang_c = Button(self.root, text="Erlang-C", command=lambda: self.update("Erlang-C"))
        self.cylcic = Button(self.root, text="Cyclic", command=lambda: self.update("Cyclic"))
        self.mm1k = Button(self.root, text="MM1K", command=lambda: self.update("MM1K"))
        self.two_servers = Button(self.root, text="Two Servers", command=lambda: self.update("TwoServers"))

        # menu Layout
        self.erlang_b.grid(row=3, column=0)
        self.erlang_c.grid(row=3, column=1)
        self.cylcic.grid(row=3, column=2)
        self.mm1k.grid(row=3, column=4)
        self.two_servers.grid(row=3, column=5)

    def update(self, method):
        if method == "Erlang-B":
            self.root.destroy()
            from erlang_b_gui import ErlangB
            erlang_menu = ErlangB(self.f_path)
            erlang_menu.root.mainloop()

        elif method == "Erlang-C":
            self.root.destroy()
            from erlang_c_gui import ErlangC
            erlang_c_menu = ErlangC(self.f_path)
            erlang_c_menu.root.mainloop()

        elif method == "Cyclic":
            self.root.destroy()
            from cyclic_gui import Cyclic
            cyclic_menu = Cyclic(self.f_path)
            cyclic_menu.root.mainloop()

        elif method == "MM1K":
            self.root.destroy()
            from mm1k_gui import MM1K
            mm1k_menu = MM1K(self.f_path)
            mm1k_menu.root.mainloop()

        elif method == "TwoServers":
            self.root.destroy()
            from two_servers_gui import TwoServers
            two_servers_menu = TwoServers(self.f_path)
            two_servers_menu.root.mainloop()

def main():
    excel_path = sys.argv[1]
    m_menu = MainMenu(excel_path)
    m_menu.root.mainloop()

if __name__ == '__main__':
    main()