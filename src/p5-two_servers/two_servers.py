# import xlsxwriter  # write results to excel workbook
import math  # factorial


def two_servers(l, u1, u2):
    utilization = -1
    p_idle = -1

    if l < u1 + u2 and u1 > u2:
        # calculate p(0,0)
        a = float(1/((u1*u2/l)*(1/l + 1)))
        inf_geo_sum = float(1/(1-(l/(u1+u2))))

        p00 = float(math.pow(1 + a*u2/l + a*u1/l+ a * inf_geo_sum, -1))

        utilization = 1 - p00
        p_idle = p00

    elif l > u1 + u2:
        utilization = 1
        p_idle = 0

    d = dict()
    d['utilization'] = utilization
    d['p_idle'] = p_idle
    
    return d
