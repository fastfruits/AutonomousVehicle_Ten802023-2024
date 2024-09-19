def turnLeft():
    basic.show_leds("""
        # # # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    motor.servo(motor.Servos.S8, 60)
def readInput():
    global infoReading, averageReading
    motor.motor_run(motor.Motors.M1, motor.Dir.CW, 30)
    motor.servo(motor.Servos.S8, 90 + Servo_Center)
    while getAverageVoltage(1) > darkThresh or getAverageVoltage(2) > darkThresh:
        pass
    if getAverageVoltage(1) > darkThresh:
        motor.servo(motor.Servos.S8, 105 + Servo_Center)
        while getAverageVoltage(1) > darkThresh:
            pass
    else:
        motor.servo(motor.Servos.S8, 75 + Servo_Center)
        while getAverageVoltage(2) > darkThresh:
            pass
    infoReading = ""
    motor.servo(motor.Servos.S8, 90 + Servo_Center)
    basic.show_leds("""
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        # # . . .
        """)
    for index in range(numBits):
        basic.pause(500)
        basic.show_leds("""
            # # . . .
            . . . . .
            . . . . .
            . . . . .
            # # . . .
            """)
        while getAverageVoltage(2) < darkThresh:
            serial.write_line("" + str(getAverageVoltage(1)) + ", " + str(getAverageVoltage(2)))
        averageReading = 0
        while getAverageVoltage(2) > darkThresh:
            basic.show_leds("""
                # # . . .
                # # . . .
                # # . . .
                # # . . .
                # # . . .
                """)
            if getAverageVoltage(1) > darkThresh:
                averageReading = 1
        if averageReading > 0:
            infoReading = "" + infoReading + "1"
            basic.show_leds("""
                . . # . .
                . . # . .
                . . # . .
                . . # . .
                . . # . .
                """)
        else:
            infoReading = "" + infoReading + "0"
            basic.show_leds("""
                . # # # .
                . # . # .
                . # . # .
                . # . # .
                . # # # .
                """)
    return infoReading

def on_button_pressed_a():
    motor.motor_run(motor.Motors.M1, motor.Dir.CW, 30)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def getAverageVoltage(sensor: number):
    global sensorAavg, sensorBavg
    sensorBList: List[number] = []
    sensorAList: List[number] = []
    if len(sensorAList) == 20:
        sensorAList.pop()
        sensorBList.pop()
    sensorAList.unshift(pins.analog_read_pin(AnalogPin.P1))
    sensorBList.unshift(pins.analog_read_pin(AnalogPin.P2))
    if sensor == 1:
        sensorAavg = 0
        for value in sensorAList:
            sensorAavg += value
        return sensorAavg / len(sensorAList)
    else:
        sensorBavg = 0
        for value2 in sensorBList:
            sensorBavg += value2
        return sensorBavg / len(sensorBList)
def turnRight():
    basic.show_leds("""
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    motor.servo(motor.Servos.S8, 110)

def on_button_pressed_b():
    motor.motor_run(motor.Motors.M1, motor.Dir.CW, 0)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

reading = ""
sensorBavg = 0
sensorAavg = 0
averageReading = 0
infoReading = ""
Servo_Center = 0
darkThresh = 0
numBits = 0
numBits = 2
getAverageVoltage(1)
serial.redirect_to_usb()
motor.motor_run(motor.Motors.M1, motor.Dir.CW, 200)
darkThresh = 950
factor = 1.5
Servo_Center = 0
motor.servo(motor.Servos.S8, 90 + Servo_Center)

def on_forever():
    global reading
    if getAverageVoltage(1) > 950 and getAverageVoltage(2) > 950:
        basic.show_leds("""
            # # . # #
            # . . . #
            . . . . .
            # . . . #
            # # . # #
            """)
        reading = readInput()
        if reading == "00":
            basic.show_leds("""
                # . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
        elif reading == "01":
            turnRight()
        elif reading == "10":
            turnLeft()
        else:
            basic.show_leds("""
                # # # # .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """)
    elif 50 < abs(getAverageVoltage(1) - getAverageVoltage(2)):
        motor.servo(motor.Servos.S8,
            Math.map(factor * (getAverageVoltage(1) - getAverageVoltage(2)),
                -1023,
                1023,
                60,
                120))
    else:
        motor.servo(motor.Servos.S8, 90 + Servo_Center)
basic.forever(on_forever)
