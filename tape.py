#!/usr/bin/python

import sys, getopt
import pigpio

def main(argv):
   pin = 0
   brightness = 0
   try:
      opts, args = getopt.getopt(argv,"hp:b:",["pin=","brightness="])
   except getopt.GetoptError:
      print 'tape.py -p <pin> -b <brightness>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'tape.py -p <pin> -b <brightness>'
         sys.exit()
      elif opt in ("-p", "--pin"):
         pin = arg
      elif opt in ("-b", "--brightness"):
         brightness = arg
   pi = pigpio.pi()
   pi.set_PWM_dutycycle(int(pin), int(brightness))
   pi.stop()

if __name__ == "__main__":
   main(sys.argv[1:])
