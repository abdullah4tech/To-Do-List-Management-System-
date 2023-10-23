import pyfiglet

def logo():
    # Enter the text you want to convert to FIGlet art
    text = "ToDo"

    # Try different FIGlet fonts
    fonts = ['doh']

    for font_name in fonts:
        font = pyfiglet.Figlet(font=font_name, width=80)  # You can adjust the width to change the font size
        figlet_text = font.renderText(text)
        print(f'Font: {font_name}\n{figlet_text}\n')
