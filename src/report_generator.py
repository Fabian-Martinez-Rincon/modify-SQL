import xlsxwriter

def generate_report(data, filename='comparacion.xlsx'):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    cell_format = workbook.add_format({'text_wrap': True, 'border': 1, 'border_color': 'black'})

    format_iguales = workbook.add_format({'bg_color': '#98FB98', 'text_wrap': True, 'border': 1, 'border_color': 'black'})
    format_diferentes = workbook.add_format({'bg_color': '#F0F8FF', 'text_wrap': True, 'border': 1, 'border_color': 'black'})
    format_nueva = workbook.add_format({'bg_color': '#FFFACD', 'text_wrap': True, 'border': 1, 'border_color': 'black'})

    headers = ['Nombre', 'Estado', 'Modificación']
    worksheet.write('A1', headers[0],cell_format)
    worksheet.write('B1', headers[1],cell_format)
    worksheet.write('C1', headers[2], cell_format)

    worksheet.set_column('A:A', 30) 
    worksheet.set_column('B:B', 20) 
    worksheet.set_column('C:C', 100)  

    for row_num, item in enumerate(data, 1):
        row_format = None
        if item['modificacion'] == "Iguales":
            row_format = format_iguales
        elif item['modificacion'] == "---" or item['modificacion'] == "Diferentes tamaños":
            row_format = format_diferentes
        else:
            row_format = format_nueva

        worksheet.write(row_num, 0, item['nombre'], row_format)
        worksheet.write(row_num, 1, item['estado'], row_format)
        worksheet.write(row_num, 2, item['modificacion'], row_format)

    worksheet.set_column('A:A', 30)
    worksheet.set_column('B:B', 10)

    workbook.close()

