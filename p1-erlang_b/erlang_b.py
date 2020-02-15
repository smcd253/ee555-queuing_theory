import xlsxwriter

workbook = xlsxwriter.Workbook('../queuing_theory.xlsx')
this_sheet = workbook.add_worksheet('Part 1')

this_sheet.write('A1', "Hello")
this_sheet.write('A2', "World!")

workbook.close()