import xlsxwriter

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()


bold = workbook.add_format({'bold': True})


worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Quantity', bold) 


worksheet.write('A2', 'Apples')  
worksheet.write('B2', 5)
worksheet.write('A3', 'Oranges')
worksheet.write('B3', 10)


workbook.close()