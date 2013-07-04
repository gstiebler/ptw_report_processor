
import pygtk
pygtk.require('2.0')
import gtk

class MainWindow:

    def __init__(self):
        
        input_folder_label = gtk.Label( "Pasta com arquivos RPT:" )
        self.input_folder_entry = gtk.Entry()
        get_input_folder_button = gtk.Button( "Abrir..." )
        input_folder_hbox = gtk.HBox( spacing = 5 )
        input_folder_hbox.pack_start(input_folder_label, False, False, 5)
        input_folder_hbox.pack_start(self.input_folder_entry, True, True, 5)
        input_folder_hbox.pack_start(get_input_folder_button, False, False, 5)
        
        window = gtk.Window()
        vbox = gtk.VBox( spacing = 5 )
        vbox.pack_end(input_folder_hbox, False, False, 5)
        
        window.add( vbox )
        window.show_all()
        
        get_input_folder_button.connect("clicked", self.on_input_folder_button_click, self.input_folder_entry )
        
    def on_input_folder_button_click( self, widget, entry ):
        folder = self.show_folder_dialog()
        entry.set_text( folder )
        
    def show_folder_dialog( self ):
        dialog = gtk.FileChooserDialog(title="Abrir arquivo", parent=None, action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER, buttons = (gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT, gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
        dialog.set_default_response(gtk.RESPONSE_OK)
        
        response = dialog.run()
        
        print response
        if response == gtk.RESPONSE_ACCEPT:
            result = dialog.get_current_folder()
        elif response == gtk.RESPONSE_CANCEL:
            result = None

        dialog.destroy()
        
        return result
        
MainWindow()                  
gtk.main()