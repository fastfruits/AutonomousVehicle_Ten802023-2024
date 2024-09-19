def on_button_pressed_a():
    motor.motor_run(motor.Motors.M1, motor.Dir.CW, 255)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_ultrasonic_object_detected_cm():
    global index, cnt, turn
    index = 0
    cnt = 0
    while makerbit.is_ultrasonic_distance_less_than(30, DistanceUnit.CM):
        motor.servo(motor.Servos.S1, turn)
        turn = turn - 10
        basic.pause(500)
        cnt = cnt + 1
    while index < cnt * 2:
        if makerbit.is_ultrasonic_distance_less_than(30, DistanceUnit.CM):
            turn = turn - 10
            motor.servo(motor.Servos.S1, turn)
            basic.pause(500)
            index = index - 1
        else:
            turn = turn + 10
            motor.servo(motor.Servos.S1, turn)
            basic.pause(500)
        index = index + 1
    basic.pause(1000)
    motor.servo(motor.Servos.S1, 90)
makerbit.on_ultrasonic_object_detected(30, DistanceUnit.CM, on_ultrasonic_object_detected_cm)

def on_button_pressed_b():
    motor.motor_run(motor.Motors.M1, motor.Dir.CCW, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

cnt = 0
index = 0
turn = 0
factor = 1.2
motor.servo(motor.Servos.S1, 90)
turn = 90
makerbit.connect_ultrasonic_distance_sensor(DigitalPin.P15, DigitalPin.P14)

def on_forever():
    pass
basic.forever(on_forever)
