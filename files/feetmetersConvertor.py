from PySimpleGUI import Window, Text, InputText, Button, WINDOW_CLOSED, popup

enterFeetText = Text('Enter Feet')
enterFeetInputText = InputText(key='enterFeetInputText')

enterInchesText = Text('Enter Inches')
enterInchesInputText = InputText(key='enterInchesInputText')

convertButton = Button('Convert', key='convertButton')
exitButton = Button('Exit', key='exitButton')
convertResult = Text(key='convertResult')

window = Window(
    'Feet Meter Convertor',
    layout=[
        [enterFeetText, enterFeetInputText],
        [enterInchesText, enterInchesInputText],
        [convertButton, exitButton, convertResult],
    ],
    font=('Helvetica', 20)
)


while True:
    event, values = window.read()

    if event == WINDOW_CLOSED or event == 'exitButton':
        break

    try:
        feet = float(values['enterFeetInputText'])
        inches = float(values['enterInchesInputText'])

        meters = feet * 0.3048 + inches * 0.0254

        window['convertResult'].update(value=f'{meters}m')
    except ValueError:
        popup('Please provide 2 numbers.', font=('Helvetica', 20))

window.close()
