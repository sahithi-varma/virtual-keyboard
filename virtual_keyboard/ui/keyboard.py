from .button import Button

keyboard = [
    list("QWERTYUIOP"),
    list("ASDFGHJKL"),
    list("ZXCVBNM")
]

key_w, key_h = 45, 45
start_x, start_y = 50, 100

def create_keyboard_buttons():
    buttons = []
    for i, row in enumerate(keyboard):
        for j, key in enumerate(row):
            buttons.append(Button(start_x + j * (key_w + 10),
                                  start_y + i * (key_h + 10),
                                  key_w, key_h, key))
    return buttons

erase_button = Button(start_x + 8 * (key_w + 10), start_y + 2 * (key_h + 10), key_w + 30, key_h, "x")
submit_button = Button(40, 400, 140, 60, "Submit")

def draw_keyboard(img, buttons):
    for btn in buttons:
        btn.draw(img)