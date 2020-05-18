import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Task was to calculate solution for the group of linear differential equations using Runge-Kutaa 4th degree method

tstart = 0
tend = 25
step = 0.03125

def func1(arg_x, arg_y, arg_z):
    return (-10*arg_x)+(10*arg_y)

def func2(arg_x, arg_y, arg_z):
    return (28*arg_x)-arg_y-(arg_x*arg_z)

def func3(arg_x, arg_y, arg_z):
    return (-8/3)*arg_z +(arg_x*arg_y)

x = []
y = []
z = []
t = []
x.append(5)
y.append(5)
z.append(5)
t.append(tstart)
while tstart <= tend:
    newx = []
    newy = []
    newz = []
    kx = []
    ky = []
    kz = []
    kx.append(func1(x[-1], y[-1], z[-1]))
    ky.append(func2(x[-1], y[-1], z[-1]))
    kz.append(func3(x[-1], y[-1], z[-1]))
    for i in range(0,3):
        if i == 2:
            newx.append(x[-1] + kx[-1] * step)
            newy.append(y[-1] + ky[-1] * step)
            newz.append(z[-1] + kz[-1] * step)
        else:
            newx.append(x[-1] + kx[-1] * step / 2)
            newy.append(y[-1] + ky[-1] * step / 2)
            newz.append(z[-1] + kz[-1] * step / 2)
        kx.append(func1(newx[-1], newy[-1], newz[-1]))
        ky.append(func2(newx[-1], newy[-1], newz[-1]))
        kz.append(func3(newx[-1], newy[-1], newz[-1]))

    x.append(x[-1] + (1/6)*(kx[-4] + 2*kx[-3] + 2*kx[-2] + kx[-1])*step)
    y.append(y[-1] + (1 / 6) * (ky[-4] + 2*ky[-3] + 2*ky[-2] + ky[-1]) * step)
    z.append(z[-1] + (1 / 6) * (kz[-4] + 2*kz[-3] + 2*kz[-2] + kz[-1]) * step)
    t.append(tstart)
    tstart += step

plt.figure(1,figsize=(10,6))
ax1 = plt.subplot(221)
ax1.plot(t, x)
plt.xlabel("Czas")
plt.ylabel("Wartość X")
ax2 = plt.subplot(222)
ax2.plot(t, y)
plt.xlabel("Czas")
plt.ylabel("Wartość Y")
ax3 = plt.subplot(223)
ax3.plot(t, z)
plt.xlabel("Czas")
plt.ylabel("Wartość Z")

ax = plt.subplot(224, projection='3d')
ax.plot(x,y,z,)
plt.xlabel("Wartość X")
plt.ylabel("Wartość Y")
ax.set_zlabel("Wartość Z")
plt.show()
