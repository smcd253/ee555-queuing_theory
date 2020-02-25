from tkinter import Tk, Label, Button, Entry, IntVar, DoubleVar, END, W, E
import math         # factorial

from openpyxl import *

# add parent directory to path so we can
# import main menu
import sys
sys.path.insert(1, '..') 

from cyclic import cyclic

class Cyclic:

    def __init__(self):
        self.root = Tk()
        self.root.title("P3: Cyclic Queuing Systems")

        # member variables
        self.p_busy = 0         # result: probability system is busy
        self.et = 0.0           # result: expected time for packet to stay in system
        self.throughput = 0.0   # result: system throughput
        self.prop_wait = 0.0    # result: proportion of time spent waiting
        self.alpha = 0.0        # input: prep time
        self.n = 0.0            # input: number of servers
        self.u = 0.0            # input: mu

        # text fields and validation for each variable
        self.alpha_entry = Entry(self.root)
        self.n_entry = Entry(self.root)
        self.u_entry = Entry(self.root)

        # text field labels
        self.alpha_label = Label(self.root, text="Desired Preparation Time: ")
        self.n_label = Label(self.root, text="Desired Number of Servers: ")
        self.u_label = Label(self.root, text="Desired Service Rate (mu): ")

        # calcualte button
        self.calculate_button = Button(self.root, text="Calculate", command=lambda: self.update("calculate"))
        self.main_menu_button = Button(self.root, text="Main Menu", command=lambda: self.update("main-menu"))

        # initialize result text field
        self.p_busy_result = DoubleVar()
        self.p_busy_result.set(self.p_busy)
        self.et_result = DoubleVar()
        self.et_result.set(self.et)
        self.throughput_result = DoubleVar()
        self.throughput_result.set(self.throughput)
        self.prop_wait_result = DoubleVar()
        self.prop_wait_result.set(self.prop_wait)

        # result text field labels
        self.p_busy_text_label = Label(self.root, text="Probability System is Busy:")
        self.p_busy_result_label = Label(self.root, textvariable=self.p_busy_result)
        self.et_text_label = Label(self.root, text="Expected Waiting Time:")
        self.et_result_label = Label(self.root, textvariable=self.et_result)
        self.prop_wait_text_label = Label(self.root, text="Proportion of Time Spent Waiting:")
        self.prop_wait_result_label = Label(self.root, textvariable=self.prop_wait_result)
        self.throughput_text_label = Label(self.root, text="System Throughput:")
        self.throughput_result_label = Label(self.root, textvariable=self.throughput_result)

        # Calculator Layout
        self.alpha_label.grid(row=0, column=0, columnspan=3, sticky=W)
        self.alpha_entry.grid(row=0, column=4, columnspan=1, sticky=E)
        self.n_label.grid(row=1, column=0, columnspan=3, sticky=W)
        self.n_entry.grid(row=1, column=4, columnspan=1, sticky=E)
        self.u_label.grid(row=2, column=0, columnspan=3, sticky=W)
        self.u_entry.grid(row=2, column=4, columnspan=1, sticky=E)
        self.calculate_button.grid(row=3, column=0)
        self.p_busy_text_label.grid(row=4, column=0, sticky=W)
        self.p_busy_result_label.grid(row=4, column=3, columnspan=2, sticky=E)
        self.et_text_label.grid(row=5, column=0, sticky=W)
        self.et_result_label.grid(row=5, column=3, columnspan=2, sticky=E)
        self.prop_wait_text_label.grid(row=6, column=0, sticky=W)
        self.prop_wait_result_label.grid(row=6, column=3, columnspan=2, sticky=E)
        self.throughput_text_label.grid(row=7, column=0, sticky=W)
        self.throughput_result_label.grid(row=7, column=3, columnspan=2, sticky=E)
        self.main_menu_button.grid(row=8, column=0)
        
    def update(self, method):
        if method == "calculate":
            self.alpha = float(self.alpha_entry.get())
            self.n = float(self.n_entry.get())
            self.u = float(self.u_entry.get())

            result = cyclic(self.n, self.u, self.alpha)
            self.p_busy = result['p_busy']
            self.et = result['et']
            self.throughput = result['throughput']
            self.prop_wait = result['prop_wait']
            self.p_busy_result.set(self.p_busy)
            self.et_result.set(self.et)
            self.throughput_result.set(self.throughput)
            self.prop_wait_result.set(self.prop_wait)

        elif method == "main-menu":
            self.root.destroy()
            from main_menu import MainMenu
            m_menu = MainMenu()
            m_menu.root.mainloop()
            
        else: # reset
            self.p_busy = 0
    
    def write_to_excel(self):
        f_name = "/Users/SwaggySpencerMcDee/Documents/ee555/mini_project/ee555-queuing_theory/queuing_theory.xlsx"
        wb = load_workbook(f_name)
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

        wb.save(f_name)
        
def main():
    cyclic_menu = Cyclic()
    cyclic_menu.root.mainloop()

if __name__ == '__main__':
    main()