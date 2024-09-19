def on_pulsed_p8_low():
    global tickCount
    tickCount += 1
pins.on_pulsed(DigitalPin.P8, PulseValue.LOW, on_pulsed_p8_low)

def ticksToInches(num: number):
    return Math.round(num * 1.75)
radio.set_group(0)
inchesToTravel = 10
tickCount = 0
numTicksToTravel = ticksToInches(inchesToTravel)
pins.set_pull(DigitalPin.P8, PinPullMode.PULL_UP)
pins.servo_write_pin(AnalogPin.P16, 90)
motor.motor_run(motor.Motors.M1, motor.Dir.CCW, 100)

def on_forever():
    if tickCount >= numTicksToTravel:
        motor.motor_run(motor.Motors.M1, motor.Dir.CCW, 0)
    radio.send_value("ticks", tickCount)
basic.forever(on_forever)