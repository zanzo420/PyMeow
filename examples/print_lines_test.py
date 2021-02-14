from pymeow import *

ov = overlay_init()
font1 = font_init(12, "Tahoma")
font2 = font_init(30, "Terminal")
font3 = font_init(18, "Comic Sans MS")
text = [
    "Hello",
    "from",
    "pyMeow",
    "=)"
]


while overlay_loop(ov):
    overlay_update(ov)
    if key_pressed(35):
        overlay_close(ov)

    font_print_lines(
        font1,
        x=1000,
        y=1000,
        lines=text,
        color=rgb("white")
    )
    font_print_lines(
        font2,
        x=500,
        y=500,
        lines=text,
        color=rgb("yellow")
    )
    font_print_lines(
        font3,
        x=1000,
        y=500,
        lines=text,
        color=rgb("blue")
    )