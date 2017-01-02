import platform, os, os.path
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
        
        # Connect button click with showBrowseFolder function
        browse_button.clicked.connect(self.showBrowseFolder)
                
        # Config the Choose Image
        choose_label = QtGui.QLabel()
        choose_label.setText("Choose Image Folder")
        
        # Config the browse label
        self.label = QtGui.QLabel("path/to/folder")
        
        # Config convert button
        convert_button = QtGui.QPushButton('Convert')
        convert_button.setFocusPolicy(QtCore.Qt.NoFocus)
        
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
        
            # Pass binary name into function. (any binary inside the houdini\bin folder)
            # This way you can grab any binary in that folder and reuse the function
            iconvert = getBinary("iconvert")
            
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
                
                # Simplify output file
                output_file = self.path + file_base + output_format
                
                # Simplify input file
                input_file = iconvert + self.path + file_name
                
                # Check if file exists
                if os.path.isfile(output_file) == False:
                
                    command = "%s %s" % (input_file, output_file)
                    
                    # Execute iconvert command
                    os.system(command)
                    
                else:
                
                    print "%s already exists, skipped" % output_file
                
        else:   # Message box to warn no path has been set
            QtGui.QMessageBox.information(self, "Heads up!", "No path was set")
            

def getBinary(binary):

    # Locate Houdini root path
    root = None
    binary_folder = None
    executable = None
    slash = None
    
    # Determine OS filepaths
    if platform.system() == "Linux":
        
        root = hou.houdiniPath()[2]
        slash = "/"
        binary_folder = slash + "bin" + slash
        executable = binary + " "
        
        # Linux houdini root path is /opt/hfs{version}/houdini
        # We need to slash /houdini
        root = root.rpartition(slash)[0]
    
    # Filepath for windows
    elif platform.system() == "Windows":
        
        root = hou.houdiniPath()[3]
        root.replace("/", "\\")
        slash = "\\"
        binary_folder = slash
        executable = binary + ".exe "
    
    # Filepath for Mac untested
    elif platform.system() == "Darwin":
    
        print "mac"
    
    # iconvert executable string
    binary_string = root + binary_folder + executable  
    
    return(binary_string)
            
dialog = MainWindow()
dialog.show()
