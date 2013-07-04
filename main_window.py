
import pygtk
pygtk.require('2.0')
import gtk

class MainWindow:

    def __init__( self, main_presenter ):
        self.presenter = main_presenter
        
        [input_folder_hbox, self.input_folder_entry] = self.__create_folder_selection( "Pasta com arquivos RPT:" )
        [output_folder_hbox, self.output_folder_entry] = self.__create_folder_selection( "Pasta para arquivos de resultado:" )
        ok_button = gtk.Button("Ok")
        
        window = gtk.Window()
        vbox = gtk.VBox( spacing = 5 )
        vbox.pack_start(input_folder_hbox, False, False, 5)
        vbox.pack_start(output_folder_hbox, False, False, 5)
        vbox.pack_start(ok_button, False, False, 5)
        
        window.add( vbox )
        window.show_all()

        ok_button.connect("clicked", self.__on_ok_clicked )
        
    def __create_folder_selection( self, label_text ):
        folder_label = gtk.Label( label_text )
        folder_entry = gtk.Entry()
        get_folder_button = gtk.Button( "Abrir..." )
        folder_hbox = gtk.HBox( spacing = 5 )
        folder_hbox.pack_start(folder_label, False, False, 5)
        folder_hbox.pack_start(folder_entry, True, True, 5)
        folder_hbox.pack_start(get_folder_button, False, False, 5)
        
        get_folder_button.connect("clicked", self.__on_folder_button_click, folder_entry )
        
        return folder_hbox, folder_entry
        
    def __on_ok_clicked( self, widget ):
        self.presenter.ok_clicked()
        
    def __on_folder_button_click( self, widget, entry ):
        folder = self.__show_folder_dialog()
        entry.set_text( folder )
        
    def __show_folder_dialog( self ):
        dialog = gtk.FileChooserDialog(title="Abrir arquivo", parent=None, action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT, gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
        dialog.set_default_response(gtk.RESPONSE_OK)
        
        response = dialog.run()
        
        result = None
        if response == gtk.RESPONSE_ACCEPT:
            result = dialog.get_current_folder()

        dialog.destroy()
        
        return result
        
    def get_input_folder( self ):
        return self.input_folder_entry.get_text()
        
    def get_output_folder( self ):
        return self.output_folder_entry.get_text()
        