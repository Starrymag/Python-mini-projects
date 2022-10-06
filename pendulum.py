#!/usr/bin/env python

from tkinter import*
from math import sin, cos, pi
import time

width = 1920
height  = 1080
r_pend = 400
r_obj = 40
r_line = r_pend - r_obj
a = 1.2
omega = 1.6

root = Tk()
c = Canvas(root, width=width, height=height, bg="white")
c.pack()

#объект
ball = None  #c.create_oval(80, 280, 120, 320, fill='green', width=2)

#оси координат
linX = c.create_line(width/2, height, width/2, 0, fill='black',
	                 arrow = LAST,width=4)
linY = c.create_line(0, height/2, width, height/2, fill='black',
	                 arrow = LAST,width=4)

#траектория
lin_circle = c.create_oval((width/2)-r_pend, (height/2)-r_pend, 
                           (width/2)+r_pend, (height/2)+r_pend)
lin_line = c.create_oval((width/2)-r_pend+r_obj, (height/2)-r_pend+r_obj,
                         (width/2)+r_pend-r_obj, (height/2)+r_pend-r_obj)
line_thread = None  #c.create_line(width/2, height/2, width/2, height/2 + r_line)

def frame ():
    global ball, line_thread, r_pend, width, height, start_time, r_obj, r_line
    
    current_time = time.clock_gettime(time.CLOCK_MONOTONIC)
    delta_time = start_time - current_time

    phi = time_in_polar(delta_time)
    
    x1 = (r_pend * cos(phi)) + width/2
    y1 = (r_pend * sin(phi)) + height/2
    
    x01_current = round(x1) - r_obj   # + x01  #- 20
    y01_current = round(y1) - r_obj   # + y01  #- 20
    x02_current = round(x1) + r_obj   # + x02  #+ 20
    y02_current = round(y1) + r_obj   # + y02  #+ 20
    
    x2_line = (r_line * cos(phi)) + width/2 
    y2_line = (r_line * sin(phi)) + height/2
    
    c.delete(ball) 
    c.delete(line_thread)
    ball = c.create_oval(x01_current, y01_current, 
                         x02_current, y02_current, fill='red', width=2)
    line_thread = c.create_line(width/2, height/2, x2_line, y2_line, width=2)   
   
    c.after(17, frame)


def time_in_polar (delta_time):
    global a, omega
    phi =  (sin(delta_time*omega) * a) + (pi/2)
    return phi

start_time = time.clock_gettime(time.CLOCK_MONOTONIC)
frame()
        
root.mainloop()