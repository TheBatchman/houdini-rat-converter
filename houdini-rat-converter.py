import platform, os
from PySide import QtCore, QtGui

class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # Set window location and title
        self.setGeometry(500, 300, 250, 110)
        self.setWindowTitle('Houdini image RAT converter')
        
        # Config browse button
        browse_button = QtGui.QPushButton('Browse')
        browse_button.setFocusPolicy(QtCore.Qt.NoFocus)
        browse_button.move(20, 20)
        
        # Connect button click with showBrowseFolder function
        browse_button.clicked.connect(self.showBrowseFolder)
        
        #self.connect(browse_button, QtCore.SIGNAL('clicked()'), self.showBrowseFolder)
        
        # Config the Choose Image
        choose_label = QtGui.QLabel()
        choose_label.setText("Choose Image Folder")
        #choose_label.move(150, 100)
        
        # Config the browse label
        self.label = QtGui.QLabel("path/to/folder")
        self.label.move(130, 20)
        
        # Config convert button
        convert_button = QtGui.QPushButton('Convert')
        convert_button.setFocusPolicy(QtCore.Qt.NoFocus)
        #browse_button.move(20, 20)
        
        # Connect button click with showBrowseFolder function
        convert_button.clicked.connect(self.startConvertion)
        
        # Add labels  & buttons
        window = QtGui.QVBoxLayout()
        window.addWidget(browse_button)
        window.addWidget(choose_label)
        window.addWidget(self.label)
        window.addWidget(convert_button)
                
        self.setLayout(window)
        
        # Set path variable to empty, to later be filled by showBroseFolder function
        self.path = None

    def showBrowseFolder(self):
    
        path = QtGui.QFileDialog.getExistingDirectory()
        
        if path:
            self.label.setText(path)
            self.path = path
            
    def startConvertion(self):
    
        if self.path:
        
            # Locate Houdini root path
            root = hou.houdiniPath()[2]
            binary_folder = None
            executable = None
        
            # Determine OS filepaths
            if platform.system() == "Linux":
            
                binary_folder = "/bin/"
                executable = "iconvert "
                
                # Linux houdini root path is /opt/hfs{version}/houdini
                # We need to slash of /houdini
                root = root.rpartition("/")[0]
            
            # Filepath for windows untested
            elif platform.system() == "Windows":
            
                inary_folder = "\\bin\\"
                executable = "iconvert.exe "
            
            # Filepath for Mac untested
            elif platform.system() == "Darwin":
            
                print "mac"
                
            # iconvert executable string
            iconvert = root + binary_folder + executable
            
            getDirInfo = QtCore.QDir(self.path)
            
            # File extentions to process
            filters = ["*.jpg", "*.tiff", "*.tga"]
            
            # Setting name filters
            getDirInfo.setNameFilters(filters)
            
            # Iterating through the files
            for entry in getDirInfo.entryInfoList():
            
                # Get file name plus extention
                file_name = "/" + entry.fileName()
                
                # Get base filename
                file_base = "/" + entry.baseName()
                
                # Get file info
                file_info = QtCore.QFileInfo(self.path + entry.fileName())
                
                # Get file extention (e.g. jpg, tiff, tga)
                file_ext = file_info.completeSuffix()
                
                # Output format
                output_format = ".rat"
            
                command = "%s%s%s %s%s%s" % (iconvert, self.path, file_name, self.path, file_base, output_format)
                
                # Execute iconvert command
                os.system(command)
                
        else:            # Message box to warn no path has been set
            QtGui.QMessageBox.information(self, "Heads up!", "No path was set")
            

dialog = MainWindow()
dialog.show()
