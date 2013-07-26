
import os

from main_window import MainWindow
from report_processor import ReportProcessor
                
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
                ReportProcessor().process_report( output_folder, reports_folder, file )

        self.window.show_message( "Processo concluído." )
