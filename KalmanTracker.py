import numpy as np
import matplotlib.pyplot as plt

# task given was to implement the kalman tracker to predict the next positions of the airplane based on the data from
# file containing series of earlier positions

x_pos = []
y_pos = []
file = open("measurements13.txt", "r")
for line in file:
    separate = line.split()
    if separate is not None:
        x_pos.append(float(separate[0]))
        y_pos.append(float(separate[1]))
file.close()
s_matrices = []
p_matrices = []
f_matrices = []
z_matrices = []
e_matrices = []
actualized_s = []
actualized_p = []
another_s_matrices = []
k_matrices = []
sensor = []
x_pos = np.array(x_pos)
y_pos = np.array(y_pos)
for i in range(len(x_pos)):
    line = np.array([x_pos[i],y_pos[i]])
    line = np.matrix(line)
    sensor.append(line)
P = np.identity(4)
P = P*5
P = np.matrix(P)
p_matrices.append(P)
Q = np.identity(2)
Q = Q*0.25
Q = np.matrix(Q)
R = np.identity(2)
R = R*2
R = np.matrix(R)
G = np.zeros((4, 2))
G[2, 0] = 1
G[3, 1] = 1
G = np.matrix(G)
H = np.zeros((2, 4))
H[0, 0] = 1
H[1, 1] = 1
H = np.matrix(H)
S = np.zeros((4,1))
S[0, 0] = x_pos[0]
S[1, 0] = y_pos[0]
S = np.matrix(S)
s_matrices.append(S)

F = np.identity(4)
F[0, 2] = 1
F[1, 3] = 1
F = np.matrix(F)


for i in range(len(x_pos)-1):
    s_matrices.append(F*s_matrices[-1])
    p_matrices.append(F*p_matrices[-1]*np.transpose(F) + G*Q*np.transpose(G))
    z_matrices.append(H*s_matrices[-1])
    e_matrices.append(sensor[i+1]-z_matrices[-1])
    another_s_matrices.append((H*p_matrices[-1]*np.transpose(H))+R)
    k_matrices.append(p_matrices[-1]*np.transpose(H)*(another_s_matrices[-1]**-1))
    s_matrices[i+1] =(s_matrices[-1]+(k_matrices[-1]*e_matrices[-1]))
    p_matrices[i+1] = (np.identity(4)-k_matrices[-1]*H)*p_matrices[-1]

filtered_x = []
filtered_y = []
s_matrices.pop(0)
for element in s_matrices:
    filtered_x.append(element[0][0,0])
    filtered_y.append(element[0][0,1])
plt.plot(x_pos,y_pos, 'x', label = 'Dane z pliku')
plt.plot(filtered_x, filtered_y)
predicted_x = []
predicted_y = []
predicted_x.append(filtered_x[-1])
predicted_y.append(filtered_y[-1])
for i in range(5):
    s_matrices.append(F*s_matrices[-1])
    p_matrices.append(F * p_matrices[-1] * np.transpose(F) + G * Q * np.transpose(G))
    predicted_x.append(s_matrices[-1][0, 0])
    predicted_y.append(s_matrices[-1][0, 1])

plt.plot(predicted_x,predicted_y, '--', label='Przewidywana pozycja')
plt.plot(predicted_x[-1],predicted_y[-1],'o', label='Ostateczna pozycja')
plt.xlabel('Położenie X')
plt.ylabel('Położenie Y')
plt.legend()
plt.show()