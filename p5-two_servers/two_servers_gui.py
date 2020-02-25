from tkinter import Tk, Label, Button, Entry, IntVar, DoubleVar, END, W, E
import math         # factorial

# add parent directory to path so we can
# import main menu
import sys
sys.path.insert(1, '..') 

from two_servers import two_servers
class TwoServers:

    def __init__(self):
        self.root = Tk()
        self.root.title("P5: Two Servers")

        # member variables
        self.utilization = 0    # result: system utilization
        self.p_idle = 0.0       # result: probability that system is idle
        self.l = 0.0            # input: arrival rate
        self.u1 = 0.0           # input: service rate of server1
        self.u2 = 0.0           # input: service rate of server2

        # text fields and validation for each variable
        self.l_entry = Entry(self.root)
        self.u1_entry = Entry(self.root)
        self.u2_entry = Entry(self.root)

        # text field labels
        self.l_label = Label(self.root, text="Desired Arrival Rate (lambda): ")
        self.u1_label = Label(self.root, text="Desired Service Rate for Server 1 (mu1): ")
        self.u2_label = Label(self.root, text="Desired Service Rate for Server 2 (mu2): ")

        # calcualte button
        self.calculate_button = Button(self.root, text="Calculate", command=lambda: self.update("calculate"))
        self.main_menu_button = Button(self.root, text="Main Menu", command=lambda: self.update("main-menu"))

        # initialize result text field
        self.utilization_result = IntVar()
        self.utilization_result.set(self.utilization)
        self.p_idle_result = DoubleVar()
        self.p_idle_result.set(self.p_idle)

        # result text field labels
        self.utilization_text_label = Label(self.root, text="System Utilization:")
        self.utilization_restul_label = Label(self.root, textvariable=self.utilization_result)
        self.p_idle_result_text_label = Label(self.root, text="Probability that System is Idle:")
        self.p_idle_result.label = Label(self.root, textvariable=self.p_idle_result)

        # Calculator Layout
        self.l_label.grid(row=0, column=0, columnspan=3, sticky=W)
        self.l_entry.grid(row=0, column=4, columnspan=1, sticky=E)
        self.u1_label.grid(row=1, column=0, columnspan=3, sticky=W)
        self.u1_entry.grid(row=1, column=4, columnspan=1, sticky=E)
        self.u2_label.grid(row=2, column=0, columnspan=3, sticky=W)
        self.u2_entry.grid(row=2, column=4, columnspan=1, sticky=E)
        self.calculate_button.grid(row=3, column=0)
        self.utilization_text_label.grid(row=4, column=0, sticky=W)
        self.utilization_restul_label.grid(row=4, column=3, columnspan=2, sticky=E)
        self.p_idle_result_text_label.grid(row=5, column=0, sticky=W)
        self.p_idle_result.label.grid(row=5, column=3, columnspan=2, sticky=E)
        self.main_menu_button.grid(row=6, column=0)
        
    def update(self, method):
        if method == "calculate":
            self.u2 = float(self.u2_entry.get())
            self.l = float(self.l_entry.get())
            self.u1 = float(self.u1_entry.get())

            result = two_servers(self.l, self.u1, self.u2)
            self.utilization = result['utilization']
            self.p_idle = result['p_idle']
            self.utilization_result.set(self.utilization)
            self.p_idle_result.set(self.p_idle)

        elif method == "main-menu":
            self.root.destroy()
            from main_menu import MainMenu
            m_menu = MainMenu()
            m_menu.root.mainloop()
            
        else: # reset
            self.utilization = 0
def main():
    two_servers_menu = TwoServers()
    two_servers_menu.root.mainloop()

if __name__ == '__main__':
    main()