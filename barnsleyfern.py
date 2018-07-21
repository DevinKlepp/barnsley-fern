# Program that produces barnsley fern image
# Devin Klepp July 21st 2018
import time
import graphics as g
import random as r

# Calculating time to see which program is faster
start_time = time.time()

xold = 0 # Initial points are at the origin
yold = 0

width = 700
height = 700

# Plotting surface
win = g.GraphWin("Barnsley Fern", width, height)
win.setBackground("black")
# −2.1820 < x < 2.6558 and 0 ≤ y < 9.9983 given plot ranges

# Looping for wanted number of points
for i in range(1, 50000):
    
    prob = r.random()
    if prob < 0.01:
        xnew = 0
        ynew = 0.16 * yold
        
    elif prob < 0.86:
        xnew =  0.85 * xold + 0.04 * yold
        ynew = -0.04 * xold + 0.85 * yold + 1.6

    elif prob < 0.93:
        xnew = 0.20 * xold - 0.26 * yold
        ynew = 0.23 * xold + 0.22 * yold + 1.6

    else:
        xnew = -0.15 * xold + 0.28 * yold
        ynew =  0.26 * xold + 0.24 * yold + 0.44
        
    xold = xnew
    yold = ynew

    win.plot(width / 2 + (xnew * 120),-1 * ynew * 65 + height, "green")
    #print(prob, xnew, ynew)
print("Original took", time.time() - start_time, "seconds to run.")
