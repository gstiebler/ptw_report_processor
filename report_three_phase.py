﻿ 
def process_three_phase( i, num_lines, workbook, report_lines, report_processor ):
    worksheet = workbook.add_worksheet('ThreePhase')
    output_line = 1
    
    bold = workbook.add_format({'bold': True})
    worksheet.write( 0, 0, 'Nome', bold )
    worksheet.write( 0, 1, 'Ik"(kA)', bold )
    worksheet.write( 0, 2, 'iDC(kA)', bold )
    worksheet.write( 0, 3, 'ip(kA)', bold )
    worksheet.write( 0, 4, 'Ib(kA)', bold )
    worksheet.write( 0, 5, 'Ik(kA)', bold )
    
    # define a largura da primeira coluna para 30
    worksheet.set_column(0, 0, 30)
    
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
        
        if i == num_lines:
            return i
        # verifica se a linha contém o título de um novo relatório
        if report_processor.has_report_title(report_lines[i]):
            return i - 1;
        
    return i
    
def process_line_three_phase( worksheet, output_line, report_lines, i ):
    # pega a iesima linha do relatório
    line = report_lines[i]
    # separa as palavras da linha
    line_parts = line.split()
    # o nome do painel eh a terceira palavra da linha
    panel_name = line_parts[2]
    # adiciona o painel na linha de saida
    worksheet.write( output_line, 0, panel_name )
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