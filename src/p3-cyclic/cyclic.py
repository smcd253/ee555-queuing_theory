import sys
import math

def cyclic(N_cli, ser_rate, prep_time):
    p_busy = -1
    ET = -1
    prop_wait = -1
    if (N_cli > 0 and ser_rate > 0 and prep_time > 0):
        # N_cli = float(2)
        # mu = float(0.8)
        # l = float(2)
        mu = ser_rate
        l = 1/prep_time
        
        C = float(N_cli)
        coef = []

        while C >= 0:
            coef.append(float(C / (l * mu)))
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
        P_busy=1 - P_zero
        ET=EN/(P_busy*mu)

    d = dict()
    d['p_busy'] = P_busy
    d['et'] = ET
    d['throughput'] = P_busy*mu
    d['prop_wait'] = ET/(ET + l)
    return d
