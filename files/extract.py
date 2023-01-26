from PySimpleGUI import Text, InputText, FileBrowse, FolderBrowse, Button, Window, WINDOW_CLOSED, Column
from zipExtractor import extract_archive

sourceText = Text('Select zip file: ')
sourceInputText = InputText(key='sourceInputText')
sourceButton = FileBrowse('Select zip files', key='sourceButton')

destinationText = Text('Select destination folder: ')
destinationInputText = InputText(key='destinationInputText')
destinationButton = FolderBrowse('Select directory', key='destinationButton')

compressButton = Button('Extract')

successMessageText = Text(key='successMessageText')

textColumn = Column([[sourceText], [destinationText]])
inputTextColumn = Column([[sourceInputText], [destinationInputText]])
buttonColumn = Column([[sourceButton], [destinationButton]])

window = Window(
    'Extract zip files',
    layout=[
        [textColumn, inputTextColumn, buttonColumn],
        [compressButton, successMessageText]
    ],
    font=('Helvetica', 20)
)

while True:
    event, values = window.read()
    if event == WINDOW_CLOSED:
        break

    sourceFilePath = values['sourceInputText']
    destinationFilePath = values['destinationInputText']

    extract_archive(sourceFilePath, destinationFilePath)

    window['successMessageText'].update(value='Successfully compressed files!')

window.close()



