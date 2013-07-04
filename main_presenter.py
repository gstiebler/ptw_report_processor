﻿
import os
from xlsxwriter.workbook import Workbook

from main_window import MainWindow

def process_report( excel_output_folder, file_name ):
    report_file_name = excel_output_folder + "/" + file_name

    # pega somente o nome do arquivo sem a extensao .RPT
    file_name_we = file_name.split('.')[0]

    # abre o arquivo de entrada
    report_file = open(report_file_name, "r")

    # abre o arquivo de saida
    workbook = Workbook(file_name_we + ".xlsx")
    worksheet = workbook.add_worksheet()

    # pega as linhas do arquivo
    report_lines = report_file.readlines()

    # pega numero de linhas do relatorio
    num_lines = len(report_lines)

    i = 0
    output_line = 0
    while i < num_lines:
        # pega a iesima linha do relatório
        line = report_lines[i]
        # verifica se a linha contem '*FAULT BUS:'
        if line.find('*FAULT BUS:') > 0:
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
            
            if len( line_parts ) < 7:
                break
            # percorre os valores da linha. O primeiro valor eh a 4a palavra
            for n in range(3, 8):
                worksheet.write( output_line, n - 2, line_parts[n] )
                
            output_line += 1
            
        # passa pra proxima linha
        i += 1
        
    # fecha o arquivo de saida
    
    workbook.close()

class MainPresenter:

    def __init__( self ):
        self.window = MainWindow( self )
        
    def ok_clicked( self ):
        reports_folder = self.window.get_input_folder()
        output_folder = self.window.get_output_folder()

        for file in os.listdir(reports_folder):
            if file.endswith(".RPT"):
                process_report( output_folder, file )
        