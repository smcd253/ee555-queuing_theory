from tkinter import Tk, Label, Button, Entry, IntVar, DoubleVar, END, W, E
import math         # factorial

from openpyxl import *

# add parent directory to path so we can
# import main menu
import sys
sys.path.insert(1, '../..') 

from mm1k import mm1k
class MM1K:

    def __init__(self, f_path):
        self.root = Tk()
        self.root.title("P4: MM1K")
        
        # excel file path
        self.f_path = f_path

        # member variables
        self.utilization = 0    # result: system utilization
        self.en = 0.0           # result: expected number of packets in system
        self.capacity = 0.0     # input: desired capacity of the system
        self.l = 0.0            # input: lambda
        self.u = 0.0            # input: mu

        # text fields and validation for each variable
        self.capacity_entry = Entry(self.root)
        self.l_entry = Entry(self.root)
        self.u_entry = Entry(self.root)

        # text field labels
        self.capacity_label = Label(self.root, text="Desired System Capacity: ")
        self.l_label = Label(self.root, text="Desired Arrival Rate (lambda): ")
        self.u_label = Label(self.root, text="Desired Service Rate (mu): ")

        # calcualte button
        self.calculate_button = Button(self.root, text="Calculate", command=lambda: self.update("calculate"))
        self.main_menu_button = Button(self.root, text="Main Menu", command=lambda: self.update("main-menu"))

        # initialize result text field
        self.utilization_result = IntVar()
        self.utilization_result.set(self.utilization)
        self.en_result = DoubleVar()
        self.en_result.set(self.en)

        # result text field labels
        self.utilization_text_label = Label(self.root, text="System Utilization:")
        self.utilization_restul_label = Label(self.root, textvariable=self.utilization_result)
        self.en_result_text_label = Label(self.root, text="Expected Number of Packets in System:")
        self.en_result.label = Label(self.root, textvariable=self.en_result)

        # Calculator Layout
        self.capacity_label.grid(row=0, column=0, columnspan=3, sticky=W)
        self.capacity_entry.grid(row=0, column=4, columnspan=1, sticky=E)
        self.l_label.grid(row=1, column=0, columnspan=3, sticky=W)
        self.l_entry.grid(row=1, column=4, columnspan=1, sticky=E)
        self.u_label.grid(row=2, column=0, columnspan=3, sticky=W)
        self.u_entry.grid(row=2, column=4, columnspan=1, sticky=E)
        self.calculate_button.grid(row=3, column=0)
        self.utilization_text_label.grid(row=4, column=0, sticky=W)
        self.utilization_restul_label.grid(row=4, column=3, columnspan=2, sticky=E)
        self.en_result_text_label.grid(row=5, column=0, sticky=W)
        self.en_result.label.grid(row=5, column=3, columnspan=2, sticky=E)
        self.main_menu_button.grid(row=6, column=0)
        
    def update(self, method):
        if method == "calculate":
            self.capacity = float(self.capacity_entry.get())
            self.l = float(self.l_entry.get())
            self.u = float(self.u_entry.get())

            result = mm1k(self.l, self.capacity, self.u)
            self.utilization = result['utilization']
            self.en = result['en']
            self.utilization_result.set(self.utilization)
            self.en_result.set(self.en)

            self.write_to_excel()
            
        elif method == "main-menu":
            self.root.destroy()
            from main_menu import MainMenu
            m_menu = MainMenu(self.f_path)
            m_menu.root.mainloop()
            
        else: # reset
            self.utilization = 0
    
    def write_to_excel(self):
        wb = load_workbook(self.f_path)
        ws = wb["Part 4"]
        data = [
            ["Inputs", "Values", "Results", "Values"],
            ["Capacity", str(self.capacity),"Utilization", str(self.utilization)],
            ["Arrival Rate", str(self.l), "E(N)", str(self.en)],
            ["Service Rate", str(self.u)]
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
    mm1k_menu = MM1K(excel_path)
    mm1k_menu.root.mainloop()

if __name__ == '__main__':
    main()