from .button import Button

platforms = ["Google", "YouTube", "Instagram"]
platform_buttons = [
    Button(40 + i*(200), 20, 180, 50, name)
    for i, name in enumerate(platforms)
]

def draw_platform_buttons(img, selected_platform):
    for btn in platform_buttons:
        active = (btn.text == selected_platform)
        btn.draw(img, active=active)

def detect_platform_selection(index_finger, current_platform):
    for btn in platform_buttons:
        if btn.is_hover(*index_finger):
            return btn.text
    return current_platform