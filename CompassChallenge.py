compass = input.compass_heading()

def on_forever():
    if compass > 10 and compass < 180:
        motor.servo(motor.Servos.S1, 60)
        basic.pause(100)
    elif compass > 180 and compass < 350:
        motor.servo(motor.Servos.S1, 110)
        basic.pause(100)
    else:
        head = 0
        motor.servo(motor.Servos.S1, head)
        basic.pause(100)
basic.forever(on_forever)