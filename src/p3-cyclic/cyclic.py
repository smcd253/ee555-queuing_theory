import sys
import math

def cyclic(N_cli, ser_rate, prep_time):
    p_busy = -1
    ET = -1
    prop_wait = -1
    if (N_cli > 0 and ser_rate > 0 and prep_time > 0):
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

    d = dict()
    d['p_busy'] = p_busy
    d['et'] = ET
    d['throughput'] = 1 / ET
    d['prop_wait'] = prop_wait
    return d
