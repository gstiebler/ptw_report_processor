 
def process_three_phase( i, num_lines, workbook, report_lines ):
    worksheet = workbook.add_worksheet()
    output_line = 0
    
    while i < num_lines:
        # pega a iesima linha do relatório
        line = report_lines[i]
        # verifica se a linha contem '*FAULT BUS:'
        if line.find('*FAULT BUS:') > 0:
            if process_line_three_phase( worksheet, output_line, report_lines, i ) == False:
                return i
            output_line += 1
            i += 5
        # passa pra proxima linha
        i += 1
        
    return i
    
def process_line_three_phase( worksheet, output_line, report_lines, i ):
    # pega a iesima linha do relatório
    line = report_lines[i]
    # separa as palavras da linha
    line_parts = line.split()
    # o nome do painel eh a terceira palavra da linha
    panel_name = line_parts[2]
    # adiciona o painel na linha de saida
    worksheet.write( output_line, 0,  panel_name )
    # pula 5 linhas
    i += 5
    # pega a linha do relatorio com os valores
    line = report_lines[i]
    # divide as palavras da linha
    line_parts = line.split()
    
    if len( line_parts ) < 8:
        return False
    # percorre os valores da linha. O primeiro valor eh a 4a palavra
    for n in range(3, 8):
        text = line_parts[n]
        worksheet.write( output_line, n - 2, text )