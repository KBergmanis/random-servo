def on_button_pressed_a():
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    servos.P1.set_angle(randint(0, 180))
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_string("RANDOM",65)

def on_forever():
    pass
basic.forever(on_forever)
