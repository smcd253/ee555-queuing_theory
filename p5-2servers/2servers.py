import xlsxwriter   # write results to excel workbook
import sys          # take in command line arguments
import math         # factorial

# inputs
u1 = float(sys.argv[1])         # arrival rate
u2 = float(sys.argv[2])         # service rate
l = float(sys.argv[3])          # l

if l < u1 and u1 > u2:
    # calculate p(0,0)
    a = float(l / (u1/l + u1 * u2))
    inf_geo_sum = float((l / u1) / (1 - l / u1))
    
    p00 = float(math.pow(1 + a * u1 + a / l + a * inf_geo_sum, -1))

    print("p(idle) = ", p00)
    print("utulization = ", 1 - p00)
else:
    print("invalid parameters")
