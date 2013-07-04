
import pygtk
pygtk.require('2.0')
import gtk

class MainWindow:

    def __init__(self):
        window = gtk.Window()
        window.show_all()
        
        gtk.main()
        
MainWindow()