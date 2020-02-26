import math         # factorial

def erlang_b(pb, l, u):
    pb_est = -1
    c = -1
    if(pb > 0 and pb <= 1 and l > 0 and u > 0 and l < u):
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
            

    d = dict()
    d['pb_actual'] = pb_est
    d['c'] = c
    return d