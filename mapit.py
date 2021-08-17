#just type or copy any location name and it will open that map little change by akhil
import webbrowser, sys ,pyperclip

sys.argv

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)