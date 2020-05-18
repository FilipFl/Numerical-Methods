import numpy as np
import matplotlib.pyplot as plt

# Task to calculate temperature of the plain element in certain points of the element, using finite difference method
# and Dirichlet boundary conditions


A = np.zeros((81, 81))
Xtop = []
Xbot = []
Yleft = []
Yright = []
B = np.zeros((81,1))
for i in range(11):
    Xtop.append([400-(i*10)])
    Yleft.append([400-(i*10)])
    Xbot.append([300-(i*10)])
    Yright.append([300-(i*10)])

for i in range(81):
    A[i, i] = -1.05
    if i-9 >= 0:
        A[i, i-9] = 1/4
    if i+9 < 81:
        A[i, i+9] = 1/4
    if i % 9 != 8:
        A[i, i+1] = 1/4
    if i % 9 != 0:
        A[i, i-1] = 1/4

row = 0
for i in range(81):
    k = i % 9
    if i == 0:
        B[i] = (-Xtop[k + 1][0] / 4) - (Yleft[row+1][0]/4) - 5
    elif i == 8:
        B[i] = -Xtop[k+1][0]/4 - Yright[row+1][0]/4 - 5
    elif i == 72:
        B[i] = -Xbot[k+1][0]/4 - Yleft[row+1][0]/4 - 5
    elif i == 80:
        B[i] = -Xbot[k + 1][0] / 4 - Yright[row + 1][0] / 4 - 5
    elif i < 9:
        B[i] = -Xtop[k+1][0]/4 - 5
    elif k == 0:
        B[i] = -Yleft[row+1][0]/4 - 5
    elif k == 8:
        B[i] = -Yright[row + 1][0] / 4 - 5
    elif i > 72:
        B[i] = -Xbot[k+1][0]/4 - 5
    else:
        B[i] = -5
    if k == 8:
        row += 1
A = np.matrix(A)
B = np.matrix(B)
X = (A**-1)*B
X = X.reshape((9, 9))
X = np.array(X)
Xtop = Xtop[1:]
Xtop = Xtop[:len(Xtop)-1]
Xbot = Xbot[1:]
Xbot = Xbot[:len(Xbot)-1]
Xbot = np.array(Xbot)
Xtop = np.array(Xtop)
Xtop = Xtop.reshape((1,9))
Xbot = Xbot.reshape((1,9))
Yleft = np.array(Yleft)
Yright = np.array(Yright)
X = np.vstack((Xtop,X))
X = np.vstack((X,Xbot))
X = np.hstack((Yleft,X))
X = np.hstack((X,Yright))
plt.imshow(X, cmap="hot", interpolation="bilinear")
plt.xlabel("Biały najcieplej, czarny najzimniej")
plt.show()
