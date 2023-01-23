from PySimpleGUI import Window, Text, InputText, FilesBrowse, FolderBrowse, Button

sourceText = Text('Select files to compress: ')
sourceInputText = InputText()
sourceButton = FilesBrowse('Select files')

destinationText = Text('Select destination folder: ')
destinationInputText = InputText()
destinationButton = FolderBrowse( 'Select directory')

compressButton = Button('Compress')

window = Window('Compress to zip files', layout=
    [
        [sourceText, sourceInputText, sourceButton],
        [destinationText, destinationInputText, destinationButton],
        [compressButton]
    ])

window.read()

window.close()
