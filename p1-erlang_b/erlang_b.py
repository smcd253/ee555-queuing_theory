# It is desired to design an Erlang B calculator for the M/M/c/c "lost calls queuing model"
# that we discussed on Friday session. The input parameters are the average arrival rate
# () in packets/min, the average service rate () in packets/min and the probability of
# blocking, P B . The output parameter should be the number of servers “c” required to
# satisfy the P B requirement. Remember that the number of servers has to be an integer.
# So if the answer from your “calculation is not an integer, you need to take the “next”
# higher integer.

import xlsxwriter   # write results to excel workbook
import sys          # take in command line arguments
import math         # factorial

# inputs
pb = float(sys.argv[1])    # probability of blocking (dropping newly arrived packets)
l = float(sys.argv[2])      # arrival rate
u = float(sys.argv[3])      # service rate

# open workbook to write input data
workbook = xlsxwriter.Workbook('../queuing_theory.xlsx')
this_sheet = workbook.add_worksheet('Part 1')

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
    

print("pb = ", pb)
print("pb_est = ", pb_est)
print("c = ", c)

# record results
this_sheet.write('A6', "Results")
this_sheet.write('A7', "Number of Servers")
this_sheet.write('B7', str(c))
this_sheet.write('A8', "Actual P(block)")
this_sheet.write('B8', str(pb_est))

# close workbook
workbook.close()