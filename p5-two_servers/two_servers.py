import xlsxwriter  # write results to excel workbook
import math  # factorial


def two_servers(l, u1, u2):

    utilization = -1
    p_idle = -1

    if l < u1 and u1 > u2:
        # calculate p(0,0)
        a = float(l/(2*((u1*u2)/l)))
        inf_geo_sum = float((l/(u1+u2))/(1-(l/(u1+u2))))

        p00 = float(math.pow(1 + a + (1/(2*(u1/l)))+(1/(2*(u2/l)))+ a * inf_geo_sum, -1))

        utilization = 1 - p00
        p_idle = p00

    d = dict()
    d['utilization'] = utilization
    d['p_idle'] = p_idle
    return d
