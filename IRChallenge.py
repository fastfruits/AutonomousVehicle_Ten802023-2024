def on_button_pressed_a():
    motor.motor_run(motor.Motors.M1, motor.Dir.CW, 50)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    motor.motor_run(motor.Motors.M1, motor.Dir.CW, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

factor = 1.2
Servo_Center = 0
motor.servo(motor.Servos.S8, 90 + Servo_Center)

def on_forever():
    if 100 < abs(pins.analog_read_pin(AnalogPin.P0) - pins.analog_read_pin(AnalogPin.P1)):
        motor.servo(motor.Servos.S8,
            Math.map(factor * (pins.analog_read_pin(AnalogPin.P0) - pins.analog_read_pin(AnalogPin.P1)),
                -1023,
                1023,
                60,
                120))
    else:
        motor.servo(motor.Servos.S8, 90 + Servo_Center)
basic.forever(on_forever)