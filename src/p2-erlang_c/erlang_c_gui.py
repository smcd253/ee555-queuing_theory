from tkinter import Tk, Label, Button, Entry, IntVar, DoubleVar, END, W, E
import math         # factorial

from openpyxl import *

# add parent directory to path so we can
# import main menu
import sys
sys.path.insert(1, '../..') 

from erlang_c import erlang_c

class ErlangC:

    def __init__(self, f_path):
        self.root = Tk()
        self.root.title("P2: Erlang-C Calculator")

        # excel file path
        self.f_path = f_path

        # member variables
        self.num_servers = 0    # result: number of servers
        self.es = 0.0           # result: expected waiting time
        self.en = 0.0           # result: expected number packets in system
        self.alpha = 0.0        # input: max waiting time
        self.epsilon = 0.0      # input: max probability waiting
        self.l = 0.0            # input: lambda
        self.u = 0.0            # input: mu

        # text fields and validation for each variable
        self.epsilon_entry = Entry(self.root)
        self.alpha_entry = Entry(self.root)
        self.l_entry = Entry(self.root)
        self.u_entry = Entry(self.root)

        # text field labels
        self.epsilon_label = Label(self.root, text="Probability of Waiting Should Not Exceed: ")
        self.alpha_label = Label(self.root, text="Waiting Time Should Not Exceed: ")
        self.l_label = Label(self.root, text="Desired Arrival Rate (lambda): ")
        self.u_label = Label(self.root, text="Desired Service Rate (mu): ")

        # calcualte button
        self.calculate_button = Button(self.root, text="Calculate", command=lambda: self.update("calculate"))
        self.main_menu_button = Button(self.root, text="Main Menu", command=lambda: self.update("main-menu"))

        # initialize result text field
        self.num_servers_result = IntVar()
        self.num_servers_result.set(self.num_servers)
        self.es_result = DoubleVar()
        self.es_result.set(self.es)
        self.en_result = DoubleVar()
        self.en_result.set(self.en)

        # result text field labels
        self.num_servers_text_label = Label(self.root, text="Number of Servers Required:")
        self.num_servers_result_label = Label(self.root, textvariable=self.num_servers_result)
        self.es_text_label = Label(self.root, text="Expected Waiting Time:")
        self.es_result_label = Label(self.root, textvariable=self.es_result)
        self.en_text_label = Label(self.root, text="Expected Number Packets in System:")
        self.en_result_label = Label(self.root, textvariable=self.en_result)

        # Calculator Layout
        self.epsilon_label.grid(row=0, column=0, columnspan=3, sticky=W)
        self.epsilon_entry.grid(row=0, column=4, columnspan=1, sticky=E)
        self.alpha_label.grid(row=1, column=0, columnspan=3, sticky=W)
        self.alpha_entry.grid(row=1, column=4, columnspan=1, sticky=E)
        self.l_label.grid(row=2, column=0, columnspan=3, sticky=W)
        self.l_entry.grid(row=2, column=4, columnspan=1, sticky=E)
        self.u_label.grid(row=3, column=0, columnspan=3, sticky=W)
        self.u_entry.grid(row=3, column=4, columnspan=1, sticky=E)
        self.calculate_button.grid(row=4, column=0)
        self.num_servers_text_label.grid(row=5, column=0, sticky=W)
        self.num_servers_result_label.grid(row=5, column=3, columnspan=2, sticky=E)
        self.es_text_label.grid(row=6, column=0, sticky=W)
        self.es_result_label.grid(row=6, column=3, columnspan=2, sticky=E)
        self.en_text_label.grid(row=7, column=0, sticky=W)
        self.en_result_label.grid(row=7, column=3, columnspan=2, sticky=E)
        self.main_menu_button.grid(row=8, column=0)
        
    def update(self, method):
        if method == "calculate":
            self.epsilon = float(self.epsilon_entry.get())
            self.alpha = float(self.alpha_entry.get())
            self.l = float(self.l_entry.get())
            self.u = float(self.u_entry.get())

            result = erlang_c(self.l, self.u, self.epsilon, self.alpha)
            self.num_servers = result['c']
            self.es = result['es']
            self.en = result['en']
            self.num_servers_result.set(self.num_servers)
            self.es_result.set(self.es)
            self.en_result.set(self.en)
            
            self.write_to_excel()

        elif method == "main-menu":
            self.root.destroy()
            from main_menu import MainMenu
            m_menu = MainMenu(self.f_path)
            m_menu.root.mainloop()
            
        else: # reset
            self.num_servers = 0
    
    def write_to_excel(self):
        wb = load_workbook(self.f_path)
        ws = wb["Part 2"]
        data = [
            ["Inputs", "Values", "Results", "Values"],
            ["Max P(wait)", str(self.epsilon),"Number of Servers", str(self.num_servers)],
            ["Max E(w)", str(self.alpha), "E(S)", str(self.es)],
            ["Arrival Rate", str(self.l),"E(N)", str(self.en)],
            ["Service Rate",str(self.u),"", ""]
        ]
        i = 1
        for v in data:
            j = 1
            for e in v:
                c = ws.cell(row = i, column = j)
                c.value = e
                j += 1
            i += 1

        wb.save(self.f_path)

def main():
    excel_path = sys.argv[1]
    erlang_c_menu = ErlangC(excel_path)
    erlang_c_menu.root.mainloop()

if __name__ == '__main__':
    main()