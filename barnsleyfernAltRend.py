# Program that produces barnsley fern image
# Devin Klepp July 21st 2018
import time
import graphics as g
import random as r

# Calculating time to see which program is faster
start_time = time.time()

xold = 0 # Initial points are at the origin
yold = 0

xnew = []
ynew = []

width = 700
height = 700

# −2.1820 < x < 2.6558 and 0 ≤ y < 9.9983 given plot ranges

# Looping for wanted number of points
for i in range(0, 50000):
    
    prob = r.random()
    if prob < 0.01:
        xnew.append(0)
        ynew.append(0.16 * yold)
        
    elif prob < 0.86:
        xnew.append(0.85 * xold + 0.04 * yold)
        ynew.append(-0.04 * xold + 0.85 * yold + 1.6)

    elif prob < 0.93:
        xnew.append(0.20 * xold - 0.26 * yold)
        ynew.append(0.23 * xold + 0.22 * yold + 1.6)

    else:
        xnew.append(-0.15 * xold + 0.28 * yold)
        ynew.append(0.26 * xold + 0.24 * yold + 0.44)
        
    xold = xnew[i]
    yold = ynew[i]
    #print(prob, xnew, ynew)

# Plotting surface
win = g.GraphWin("Barnsley Fern", width, height)
win.setBackground("black")
for i in range(len(xnew)):
    win.plot(width / 2 + (xnew[i] * 120),-1 * ynew[i] * 65 + height, "green")
#print(prob, xnew, ynew)

print("Alt Render took", time.time() - start_time, "seconds to run.")
