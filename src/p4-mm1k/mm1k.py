
def mm1k(_lambda, capacity, mu):
    utilization = -1
    EN = -1
    if(_lambda > 0 and mu > 0 and capacity > 0): 
        C = capacity
        coef =[]
        for i in range(int(C)):
            coef.append(((1-(i/capacity))*_lambda)/mu)


        _sum = 0
        for i in range(int(capacity)-1):
            coef[i+1] *= coef[i]
            _sum = coef[i+1]+_sum

        _sum=float(coef[0]+_sum)

        P_zero = float(1/(_sum+1))
        P = []
        EN = 0

        for i in range(int(capacity)):
            P.append(coef[i]*P_zero)
            EN += P[i]*(i+1)

        utilization = 1-P_zero

    d = dict()
    d['utilization'] = utilization
    d['en'] = EN
    return d
