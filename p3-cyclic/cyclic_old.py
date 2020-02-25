import xlsxwriter
import sys
import math

N_cli = float(sys.argv[1])
sep_rate = float(sys.argv[2])
prep_time = float(sys.argv[3])

C = float(N_cli)
coef = []

while C >= 0:
    coef.append(float(C / (prep_time * sep_rate)))
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

print("p(busy) = ", 1 - P_zero)
print("utilization = ", 1 / prep_time)
print("E(T) = ", EN / (1 / prep_time))
