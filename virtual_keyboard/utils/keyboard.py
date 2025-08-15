import cv2

class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = (x, y, w, h)
        self.text = text

    def draw(self, img, active=False):
        x, y, w, h = self.rect
        color = (0, 255, 0) if active else (255, 0, 0)
        cv2.rectangle(img, (x, y), (x+w, y+h), color, cv2.FILLED)
        cv2.putText(img, self.text, (x+10, y+40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    def is_hover(self, px, py):
        x, y, w, h = self.rect
        return x < px < x+w and y < py < y+h

keyboard = [
    list("QWERTYUIOP"),
    list("ASDFGHJKL"),
    list("ZXCVBNM")
]

key_w, key_h = 45, 45
start_x, start_y = 50, 100

buttons = []
for i, row in enumerate(keyboard):
    for j, key in enumerate(row):
        buttons.append(Button(start_x + j * (key_w + 10),
                              start_y + i * (key_h + 10),
                              key_w, key_h, key))

erase_button = Button(start_x + 8 * (key_w + 10), start_y + 2 * (key_h + 10), key_w + 30, key_h, "x")
platform_buttons = [
    Button(40 + i*(200), 20, 180, 50, name)
    for i, name in enumerate(["Google", "YouTube", "Instagram"])
]
submit_button = Button(40, 400, 140, 60, "Submit")