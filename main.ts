input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    servos.P1.setAngle(randint(0, 180))
})
basic.showString("RANDOM", 65)
