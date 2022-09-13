def on_button_pressed_a():
    global X
    X = (a * X + b) % c
    basic.show_number(X)
input.on_button_pressed(Button.A, on_button_pressed_a)

c = 0
b = 0
a = 0
X = 0
X = 12
a = 16
b = 20
c = 23