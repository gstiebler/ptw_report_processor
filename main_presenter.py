
import os
from xlsxwriter.workbook import Workbook

from main_window import MainWindow
import report_three_phase
import report_unbalanced_fault

def process_report( excel_output_folder, reports_folder, file_name ):
    report_file_name = reports_folder + "/" + file_name

    # pega somente o nome do arquivo sem a extensao .RPT
    file_name_we = file_name.split('.')[0]

    # abre o arquivo de entrada
    report_file = open(report_file_name, "r")
    print "Abrindo file " + report_file_name

    # abre o arquivo de saida
    excel_output_file = excel_output_folder + "/" + file_name_we + ".xlsx"
    print "Gerando arquivo " + excel_output_file
    workbook = Workbook( excel_output_file )

    # pega as linhas do arquivo
    report_lines = report_file.readlines()

    # pega numero de linhas do relatorio
    num_lines = len(report_lines)

    i = 0
    while i < num_lines:
        # pega a iesima linha do relatório
        line = report_lines[i]
        if line.find('T H R E E   P H A S E   I E C  6 0 9 0 9   F A U L T   R E P O R T') > 0:
            i = report_three_phase.process_three_phase( i, num_lines, workbook, report_lines )
        elif line.find('U N B A L A N C E D   I E C  6 0 9 0 9   F A U L T   R E P O R T') > 0:
            i = report_unabalanced_fault.process_unabalanced_fault( i, num_lines, workbook, report_lines )    
            
        # passa pra proxima linha
        i += 1
        
    # fecha o arquivo de saida
    workbook.close()             
                
class MainPresenter:

    def __init__( self ):
        self.window = MainWindow( self )
        
        path_input = os.path.dirname(__file__) + "\\relatorios_rpt"
        path_output = os.path.dirname(__file__) + "\\saida_excel"
        
        if os.path.isdir(path_input):
            self.window.set_input_folder(path_input)
            
        if os.path.isdir(path_output):
            self.window.set_output_folder(path_output)
        
    def ok_clicked( self ):
        reports_folder = self.window.get_input_folder()
        output_folder = self.window.get_output_folder()

        for file in os.listdir(reports_folder):
            if file.endswith(".RPT"):
                process_report( output_folder, reports_folder, file )

        self.window.show_message( "Processo concluído." )
