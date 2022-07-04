# import curses and GPIO
import curses
import pigpio
#pwm gpio pins
pwm1 = 12
pwm2 = 13
pwm3 = 18
pwm4 = 19
#dir gpio pins
dir1 = 5
dir2 = 6
dir3 = 23
dir4 = 24
pi = pigpio.pi()

pi.write(dir1, 1)
pi.write(dir2, 1)
pi.write(dir3, 1)
pi.write(dir4, 1)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(1)

try:
        while 1:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                pi.write(pwm1,0)
                pi.write(pwm2,1)
                pi.write(pwm3,1)
                pi.write(pwm4,0)
            elif char == curses.KEY_DOWN:
                pi.write(pwm1,1)
                pi.write(pwm2,0)
                pi.write(pwm3,0)
                pi.write(pwm4,1)
            elif char == curses.KEY_RIGHT:
                pi.write(pwm1,1)
                pi.write(pwm2,1)
                pi.write(pwm3,0)
                pi.write(pwm4,1)
            elif char == curses.KEY_LEFT:
                pi.write(pwm1,0)
                pi.write(pwm2,0)
                pi.write(pwm3,1)
                pi.write(pwm4,1)
            elif char == curses.KEY_BACKSPACE:
                pi.write(pwm1,1)
                pi.write(pwm2,0)
                pi.write(pwm3,1)
                pi.write(pwm4,0)
            elif char == curses.KEY_SHOME:    
                pi.write(pwm1,0)
                pi.write(pwm2,1)
                pi.write(pwm3,0)
                pi.write(pwm4,1)
            elif char == 10:
                pi.write(pwm1,0)
                pi.write(pwm2,0)
                pi.write(pwm3,0)
                pi.write(pwm4,0)
 
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
