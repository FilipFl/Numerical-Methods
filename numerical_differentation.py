import numpy as np
import math

# task given was to implement various numerical methods of solving differential equations including Euler's method and Heun method

def func(argt, argy):
    return argy*(1-argy)*argt


def analytic(time):
    # C = 1
    return math.e**((time**2)/2)/(1+math.e**((time**2)/2))


def euler(start,stop, h):
    curr_time = start
    y = 0.5
    while curr_time <= stop:
        y = y + func(curr_time, y)*h
        curr_time += h
    return y


def heun(start, stop, h):
    last_der = func(start, 0.5)
    curr_time = start
    y = 0.5
    while curr_time <= stop:
        naive_y = y + func(curr_time, y)*h
        der_y = func(curr_time,naive_y)
        mid_der = (last_der+der_y)/2
        y = y + mid_der*h
        last_der = mid_der
        curr_time += h
    return y


def midpoint(start, stop, h):
    curr_time = start
    y = 0.5
    while curr_time <  stop:
        naive_y = y + func(curr_time, y) * (h/2)
        der = func(curr_time, naive_y)
        y = y + der*h
        curr_time += h
    return y


start_time = 0
print("Czas początkowy ustawiony na 0.")
end_time = int(input("Podaj czas końcowy :"))
n = 100
step = (end_time-start_time)/n
start_condition = 1/2
print("Dla podanego czasu końcowego i współczynnika n=" + str(n) +" osiągnięto następujące wyniki:")
print("Metodą analityczną: " + str(analytic(end_time)))
print("Metodą Eulera: " + str(euler(start_time, end_time, step)))
print("Metodą Heuna: " + str(heun(start_time, end_time, step)))
print("Metoda punktu środkowego :" + str(midpoint(start_time, end_time, step)))
