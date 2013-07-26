
from xlsxwriter.workbook import Workbook

import report_three_phase
import report_unbalanced_fault  

class ReportProcessor:

    def process_report( self, excel_output_folder, reports_folder, file_name ):
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
                i = report_three_phase.process_three_phase( i, num_lines, workbook, report_lines, self )
            elif line.find('U N B A L A N C E D   I E C  6 0 9 0 9   F A U L T   R E P O R T') > 0:
                i = report_unbalanced_fault.process_unbalanced_fault( i, num_lines, workbook, report_lines, self )    
                
            # passa pra proxima linha
            i += 1
            
        # fecha o arquivo de saida
        workbook.close()     
        
        
    def has_report_title(self, line):
        if line.find('T H R E E   P H A S E   I E C  6 0 9 0 9   F A U L T   R E P O R T') > 0:
            return True
        elif line.find('U N B A L A N C E D   I E C  6 0 9 0 9   F A U L T   R E P O R T') > 0:
            return True
        
        return False
            