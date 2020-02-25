import xlsxwriter

def mm1k(_lambda, capacity, mu):
    utilization = -1
    EN = -1
    if(_lambda > 0 and mu > 0 and _lambda < u and capacity > 0): 
        # open workbook to write input data
        workbook = xlsxwriter.Workbook('../queuing_theory.xlsx')
        this_sheet = workbook.add_worksheet('Part 4')

        # write input data to worksheet
        this_sheet.write('A1', "Inputs")
        this_sheet.write('A2', "Number of Capacity")
        this_sheet.write('A3', "Arrival Rate")
        this_sheet.write('A4', "Service Rate")

        this_sheet.write('B1', "Values")
        this_sheet.write('B2', str(capacity))
        this_sheet.write('B3', str(_lambda))
        this_sheet.write('B4', str(mu))

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

        # record results
        this_sheet.write('A6', "Results")
        this_sheet.write('A7', "Utilization")
        this_sheet.write('B7', str(utilization))
        this_sheet.write('A8', "E(N)")
        this_sheet.write('B8', str(EN))

        # close workbook
        workbook.close()

    d = dict()
    d['utilization'] = utilization
    d['en'] = EN
    return d
