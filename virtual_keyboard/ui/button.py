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