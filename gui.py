from tkinter import Tk, Label, Button, Entry, IntVar, DoubleVar, END, W, E
import math         # factorial

from erlang_b_new import erlang_b
class ErlangB:

    def __init__(self, master):
        self.master = master
        master.title("P1: Erlang-B Calculator")

        # member variables
        self.num_servers = 0    # result: number of servers
        self.pb_actual = 0.0    # result: actual probability of blocking
        self.pb = 0.0           # input: desired probability of blocking
        self.l = 0.0            # input: lambda
        self.u = 0.0            # input: mu

        # text fields and validation for each variable
        self.pb_entry = Entry(master)
        self.l_entry = Entry(master)
        self.u_entry = Entry(master)

        # text field labels
        self.pb_label = Label(master, text="Desired Probability of Blocking: ")
        self.l_label = Label(master, text="Desired Arrival Rate (lambda): ")
        self.u_label = Label(master, text="Desired Service Rate (lambda): ")

        # calcualte button
        self.calculate_button = Button(master, text="Calculate", command=lambda: self.update("calculate"))

        # initialize result text field
        self.num_servers_result = IntVar()
        self.num_servers_result.set(self.num_servers)
        self.pb_actual_result = DoubleVar()
        self.pb_actual_result.set(self.pb_actual)

        # result text field labels
        self.num_servers_text_label = Label(master, text="Number of Servers Required:")
        self.num_servers_result_label = Label(master, textvariable=self.num_servers_result)
        self.pb_actual_text_label = Label(master, text="Actual Probability of Blocking:")
        self.pb_actual_result_label = Label(master, textvariable=self.pb_actual_result)

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

    def update(self, method):
        if method == "calculate":

            self.pb = float(self.pb_entry.get())
            self.l = float(self.l_entry.get())
            self.u = float(self.u_entry.get())

            result = erlang_b(self.pb, self.l, self.u)
            self.num_servers = result['c']
            self.pb_actual = result['pb_actual']

        else: # reset
            self.num_servers = 0

        self.num_servers_result.set(self.num_servers)
        self.pb_actual_result.set(self.pb_actual)

root = Tk()
my_gui = ErlangB(root)
root.mainloop()