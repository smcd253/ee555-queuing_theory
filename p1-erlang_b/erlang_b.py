import xlsxwriter   # write results to excel workbook
import math         # factorial

def erlang_b(pb, l, u):
    pb_est = -1
    c = -1
    if(pb > 0 and pb <= 1 and l > 0 and u > 0 and l < u):
        # open workbook to write input data
        workbook = xlsxwriter.Workbook("/Users/SwaggySpencerMcDee/Documents/ee555/mini_project/ee555-queuing_theory/queuing_theory.xlsx")
        this_sheet = workbook.add_worksheet("Part 1")

        # write input data to worksheet
        this_sheet.write('A1', "Inputs")
        this_sheet.write('A2', "Desired P(block)")
        this_sheet.write('A3', "Arrival Rate")
        this_sheet.write('A4', "Service Rate")

        this_sheet.write('B1', "Values")
        this_sheet.write('B2', str(pb))
        this_sheet.write('B3', str(l))
        this_sheet.write('B4', str(u))


        # solve for number of servers needed (estimate pb)
        c = 0
        pb_est = 1
        series = [c]

        while (pb_est > pb):
            c += 1
            series.append(c)
            pb_over_p0 = float(math.pow(l/u, c) * (1/math.factorial(c)))
            geo_sum = 0.0
            for k in series:
                geo_sum += float(math.pow(l/u, k) * (1/math.factorial(k)))
            
            pb_est = float(pb_over_p0/geo_sum)
            

        # record results
        this_sheet.write('A6', "Results")
        this_sheet.write('A7', "Number of Servers")
        this_sheet.write('B7', str(c))
        this_sheet.write('A8', "Actual P(block)")
        this_sheet.write('B8', str(pb_est))

        # close workbook
        workbook.close()

    d = dict()
    d['pb_actual'] = pb_est
    d['c'] = c
    return d