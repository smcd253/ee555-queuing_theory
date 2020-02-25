# It is desired to design an Erlang C calculator for the M/M/c "delayed calls queuing
# model" that we discussed on Friday session. The input parameters are the average
# arrival rate () in packets/min, the average service rate () in packets/min. In addition,
# you are given the following two “input constraints”:
# a. The probability that an arriving Packet will find all servers busy (i.e. P (W > 0))
# should not exceed  where  is an input parameter.
# b. Given that an arriving packet must wait, the average waiting time should not exceed
#  minutes where  is an input parameter. Hint: This is conditional expectations.
# Review_cond EE503)
# The outputs of your calculator should be the number of servers required to satisfy
# the above requirements/constraints. In addition, your calculator should enable me to
# find the following averages: The average number of busy servers and the average
# number of packets in the system (both waiting and being served

import xlsxwriter   # write results to excel workbook
import sys          # take in command line arguments
import math         # factorial

def erlang_c(l, u, epsilon, alpha):
    # open workbook to write input data
    workbook = xlsxwriter.Workbook('../queuing_theory.xlsx')
    this_sheet = workbook.add_worksheet('Part 2')

    # write input data to worksheet
    this_sheet.write('A1', "Inputs")
    this_sheet.write('A2', "Arrival Rate")
    this_sheet.write('A3', "Service Rate")
    this_sheet.write('A4', "P(W > 0) Less Than")
    this_sheet.write('A5', "E(W) Less Than")

    this_sheet.write('B1', "Values")
    this_sheet.write('B2', str(l))
    this_sheet.write('B3', str(u))
    this_sheet.write('B4', str(epsilon))
    this_sheet.write('B5', str(alpha))

    # solve for number of servers needed (estimate pb)
    c = 0
    pw = 1.0
    ew_cond = sys.float_info.max 
    series = [c]

    while (pw > epsilon or ew_cond > alpha):
        c += 1

        # calculate a
        a = 0.0

        # sum from 0 to c - 1
        for k in series:
            a += float(math.pow(l/u, k) * (1/math.factorial(k)))
        #calculate b
        term1 = float(math.pow(l/u, c) * (1/math.factorial(c)))
        rho = float(l/(c*u))
        term2 = float(1.0 - rho)
        b = float(term1 / term2)
        # calcualte p0
        p0 = float((math.sqrt(math.pow(a, 2) + 4*b) - a) / 2*b)
        # calculate pc
        pc = term1 * p0
        # recalculate pw
        pw = float(pc / term2)

        # recaculate ew_cond | w > o = ew_cond / pw
        ew_cond = float(pc * rho / math.pow(1.0 - rho, 2)) / pw 

        # append series at end of loop so a is sum from 0 to c - 1
        series.append(c) 
        
    en = float(rho / (1 - rho))
    es = float(rho/l)

    # record results
    this_sheet.write('A6', "Results")
    this_sheet.write('A7', "Number of Servers")
    this_sheet.write('B7', str(c))
    this_sheet.write('A8', "E(S)")
    this_sheet.write('B8', str(es))
    this_sheet.write('A9', "E(N)")
    this_sheet.write('B9', str(en))

    # close workbook
    workbook.close()

    d = dict()
    d['c'] = c
    d['es'] = es
    d['en'] = en
    return d
