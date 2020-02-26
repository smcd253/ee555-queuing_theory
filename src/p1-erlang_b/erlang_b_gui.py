from tkinter import Tk, Label, Button, Entry, IntVar, DoubleVar, END, W, E
import math         # factorial

from openpyxl import *

# add parent directory to path so we can
# import main menu
import sys
sys.path.insert(1, '../..') 

from erlang_b import erlang_b
class ErlangB:

    def __init__(self, f_path):
        self.root = Tk()
        self.root.title("P1: Erlang-B Calculator")

        # excel file path
        self.f_path = f_path

        # member variables
        self.num_servers = 0    # result: number of servers
        self.pb_actual = 0.0    # result: actual probability of blocking
        self.pb = 0.0           # input: desired probability of blocking
        self.l = 0.0            # input: lambda
        self.u = 0.0            # input: mu

        # text fields and validation for each variable
        self.pb_entry = Entry(self.root)
        self.l_entry = Entry(self.root)
        self.u_entry = Entry(self.root)

        # text field labels
        self.pb_label = Label(self.root, text="Desired Probability of Blocking: ")
        self.l_label = Label(self.root, text="Desired Arrival Rate (lambda): ")
        self.u_label = Label(self.root, text="Desired Service Rate (mu): ")

        # calcualte button
        self.calculate_button = Button(self.root, text="Calculate", command=lambda: self.update("calculate"))
        self.main_menu_button = Button(self.root, text="Main Menu", command=lambda: self.update("main-menu"))

        # initialize result text field
        self.num_servers_result = IntVar()
        self.num_servers_result.set(self.num_servers)
        self.pb_actual_result = DoubleVar()
        self.pb_actual_result.set(self.pb_actual)

        # result text field labels
        self.num_servers_text_label = Label(self.root, text="Number of Servers Required:")
        self.num_servers_result_label = Label(self.root, textvariable=self.num_servers_result)
        self.pb_actual_text_label = Label(self.root, text="Actual Probability of Blocking:")
        self.pb_actual_result_label = Label(self.root, textvariable=self.pb_actual_result)

        # Calculator Layout
        self.pb_label.grid(row=0, column=0, columnspan=3, sticky=W)
        self.pb_entry.grid(row=0, column=4, columnspan=1, sticky=E)
        self.l_label.grid(row=1, column=0, columnspan=3, sticky=W)
        self.l_entry.grid(row=1, column=4, columnspan=1, sticky=E)
        self.u_label.grid(row=2, column=0, columnspan=3, sticky=W)
        self.u_entry.grid(row=2, column=4, columnspan=1, sticky=E)
        self.calculate_button.grid(row=3, column=0)
        self.num_servers_text_label.grid(row=4, column=0, sticky=W)
        self.num_servers_result_label.grid(row=4, column=3, columnspan=2, sticky=E)
        self.pb_actual_text_label.grid(row=5, column=0, sticky=W)
        self.pb_actual_result_label.grid(row=5, column=3, columnspan=2, sticky=E)
        self.main_menu_button.grid(row=6, column=0)
        
    def update(self, method):
        if method == "calculate":
            self.pb = float(self.pb_entry.get())
            self.l = float(self.l_entry.get())
            self.u = float(self.u_entry.get())

            result = erlang_b(self.pb, self.l, self.u)
            self.num_servers = result['c']
            self.pb_actual = result['pb_actual']
            self.num_servers_result.set(self.num_servers)
            self.pb_actual_result.set(self.pb_actual)

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
        ws = wb["Part 1"]
        data = [
            ["Inputs", "Values", "Results", "Values"],
            ["Max P(blocking)", str(self.pb),"Number of Servers", str(self.num_servers)],
            ["Arrival Rate", str(self.l), "P(blocking)", str(self.pb_actual)],
            ["Service Rate", str(self.u),"", ""]
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
    erlang_menu = ErlangB(excel_path)
    erlang_menu.root.mainloop()

if __name__ == '__main__':
    main()