import time

import RPi.GPIO as GPIO
from flask import Flask, render_template
from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_led as led
from hal import hal_input_switch as input_switch
from hal import hal_dc_motor as motor
from hal import hal_servo as servo
from hal import hal_usonic as usonic
from hal import hal_moisture_sensor as moisture_sensor


app = Flask(__name__)


@app.route("/")
def index():

    templateData = {
        'title': 'ET0735 - Python Flask Raspberry Pi Demo',

    }
    return render_template('raspberry_pi.html', **templateData)




@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'ledRed':
        if action == "on":
            led.set_output(1, 1)
        elif action == "off":
            led.set_output(1, 0)

    elif deviceName == 'motor':
        if action == "on":
            motor.set_motor_speed(100)
        elif action == "off":
            motor.set_motor_speed(0)

    elif deviceName == 'servo':
        if action == "on":
            servo.set_servo_position(0)
        elif action == "off":
            servo.set_servo_position(90)


    elif deviceName == 'sensor':
        if action == "refresh":
            usonic_dist = usonic.get_distance()
    elif deviceName == 'sensor':
        if action == "refresh":
            humid_value = temp_humid_sensor.read_temp_humidity()
    elif deviceName == 'sensor':
        if action == "refresh":
            wet_or_dry = moisture_sensor.read_sensor()




    # Read Sensors Status
    buttonSts = input_switch.read_slide_switch()
    usonic_dist = usonic.get_distance()
    humid_value= temp_humid_sensor.read_temp_humidity()
    wet_or_dry=moisture_sensor.read_sensor()
    temp=str(humid_value[0])
    humi=str(humid_value[1])
    wetdry=wet_or_dry
    if wetdry==False:
        status="Dry"
    else:
        status="Wet"
    if buttonSts==0:
        buttonSts="unlocked"
    else:
        buttonSts = "locked"
    if usonic_dist<10:
        dis="open"
    else:
        dis="close"
    templateData = {
        'title': 'ET0735 - Python Flask Raspberry Pi Demo',
        'button': buttonSts,
        'usonic_dist': dis,
        'Humidity': humi,
        'Temperature': temp,
        'Moisture_status': status,
    }

    return render_template('raspberry_pi.html', **templateData)
def main():
    led.init()
    input_switch.init()
    motor.init()
    servo.init()
    usonic.init()
    temp_humid_sensor.init()
    moisture_sensor.init()

    # Run Python Flask Web Server
    app.run(host='192.168.0.100', port=80, debug=True)

if __name__ == "__main__":
    main()
