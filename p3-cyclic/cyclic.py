import xlsxwriter
import sys
import math

def cyclic(N_cli, ser_rate, prep_time):
     # open workbook to write input data
    workbook = xlsxwriter.Workbook('../queuing_theory.xlsx')
    this_sheet = workbook.add_worksheet('Part 3')

    # write input data to worksheet
    this_sheet.write('A1', "Inputs")
    this_sheet.write('A2', "Number of Clients")
    this_sheet.write('A3', "Service Rate")
    this_sheet.write('A4', "Preparation Time")

    this_sheet.write('B1', "Values")
    this_sheet.write('B2', str(N_cli))
    this_sheet.write('B3', str(ser_rate))
    this_sheet.write('B4', str(prep_time))

    C = float(N_cli)
    coef = []

    while C >= 0:
        coef.append(float(C / (prep_time * ser_rate)))
        C = C - 1

    _sum = 0
    for i in range(int(N_cli)):
        coef[i + 1] *= coef[i]
        _sum += coef[i]

    P_zero = float(1 / (_sum + 1))

    P = []
    EN = 0
    for i in range(int(N_cli)):
        P.append(coef[i] * P_zero)
        EN += P[i] * (i + 1)
        ET=float(EN / (1 / prep_time))
    
    p_busy = 1 - P_zero
    utilization = 1 / prep_time
    et = EN / (1 / prep_time)
    prop_wait = (ET-(1/ser_rate))/ET 

    # record results
    this_sheet.write('A6', "Results")
    this_sheet.write('A7', "Probability Busy")
    this_sheet.write('B7', str(p_busy))
    this_sheet.write('A8', "E(T)")
    this_sheet.write('B8', str(ET))
    this_sheet.write('A9', "Throughput")
    this_sheet.write('B9', str(1 / ET))
    this_sheet.write('A10', "Proportion Waiting")
    this_sheet.write('B10', str(prop_wait))

    # close workbook
    workbook.close()

    d = dict()
    d['p_busy'] = p_busy
    d['et'] = ET
    d['throughput'] = 1 / ET
    d['prop_wait'] = prop_wait
    return d
