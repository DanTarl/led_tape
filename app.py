#!flask/bin/python
from flask import Flask
import pigpio
import math
import time
# import sys

app = Flask(__name__)
#pigpio
#pi = pigpio.pi()
#pi.set_PWM_dutycycle(int(sys.argv[1]), 0)
#pi.stop()

@app.route('/set/<int:pin>/<int:brightness>')
def set(pin, brightness):
    real_brightness = math.ceil(brightness * 2.55)
    pi = pigpio.pi()
    current = math.ceil(pi.get_PWM_dutycycle(int(pin)))
    if current < real_brightness:
      for x in range(int(current), int(real_brightness)):
        pi.set_PWM_dutycycle(int(pin), int(x))
        time.sleep(0.1)
    else:
      for x in range(int(current), int(real_brightness), -1):
        pi.set_PWM_dutycycle(int(pin), int(x))
        time.sleep(0.1)
    pi.stop()
    return "Success"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
