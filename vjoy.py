import pyvjoy
import time

#Pythonic API, item-at-a-time

j = pyvjoy.VJoyDevice(1)

#turn button number 15 on
j.set_button(15,1)
time.sleep(1)
#Notice the args are (buttonID,state) whereas vJoy's native API is the other way around.


#turn button 15 off again
j.set_button(15,0)
time.sleep(1)


#Set X axis to fully left
j.set_axis(pyvjoy.HID_USAGE_X, 0x1)
time.sleep(1)

#Set X axis to fully right
j.set_axis(pyvjoy.HID_USAGE_X, 0x8000)
time.sleep(1)

#Also implemented:

j.reset()
j.reset_buttons()
j.reset_povs()
time.sleep(1)


#The 'efficient' method as described in vJoy's docs - set multiple values at once

j.data
# >>> <pyvjoy._sdk._JOYSTICK_POSITION_V2 at 0x....>


j.data.lButtons = 19 # buttons number 1,2 and 5 (1+2+16)
j.data.wAxisX = 0x2000 
j.data.wAxisY= 0x7500

#send data to vJoy device
j.update()
time.sleep(1)


#Lower-level API just wraps the functions in the DLL as thinly as possible, with some attempt to raise exceptions instead of return codes.