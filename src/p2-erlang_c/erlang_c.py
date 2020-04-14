# It is desired to design an Erlang C calculator for the M/M/c "delayed calls queuing
# model" that we discussed on Friday session. The input parameters are the average
# arrival rate () in packets/min, the average service rate () in packets/min. In addition,
# you are given the following two “input constraints”:
# a. The probability that an arriving Packet will find all servers busy (i.e. P (W > 0))
# should not exceed  where  is an input parameter.
# b. Given that an arriving packet must wait, the average waiting time should not exceed
#  minutes where  is an input parameter. Hint: This is conditional expectations.
# Review_cond EE503)
# The outputs of your calculator should be the number of servers required to satisfy
# the above requirements/constraints. In addition, your calculator should enable me to
# find the following averages: The average number of busy servers and the average
# number of packets in the system (both waiting and being served

import sys
import math         # factorial

def erlang_c(l, u, epsilon, alpha):
    c = -1
    es = -1
    en = -1
    if(epsilon > 0 and epsilon <= 1 and alpha > 0 and l > 0 and u > 0):
        # solve for number of servers needed (estimate pb)
        c = 0
        pw = 1.0
        ew_cond = sys.float_info.max 
        series = [c]

        while (pw > epsilon or ew_cond > alpha):
            c += 1

            # calculate a
            a = 0.0

            # sum from 0 to c - 1
            for k in series:
                a += float(math.pow(l/u, k) * (1/math.factorial(k)))
            #calculate b
            term1 = float(math.pow(l/u, c) * (1/math.factorial(c)))
            rho = float(l/(c*u))
            term2 = float(1.0 - rho)
            b = float(term1 / term2)
            # calcualte p0
            p0 = float((math.sqrt(abs(math.pow(a, 2) + 4*b) - a)) / 2*b)
            # calculate pc
            pc = term1 * p0
            # recalculate pw
            pw = float(pc / term2)

            # recaculate ew_cond | w > o = ew_cond / pw
            ew_cond = float(pc * rho / math.pow(1.0 - rho, 2)) / pw 

            # append series at end of loop so a is sum from 0 to c - 1
            series.append(c) 
            
        en = float(rho / (1 - rho))
        es = float(rho/l)

    d = dict()
    d['c'] = c
    d['es'] = es
    d['en'] = en
    return d
