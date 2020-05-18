import math

# task given was to implement various methods of numerical integration including gaussian quadrature
# Richardson method and Romberg method

def analitically(start, stop):
    return ((-0.00427*(start**5))-(0.18585*(start**4))+((0.1465/3)*(start**3))+(3.9335*(start**2))+(5.721*start))-\
           ((-0.00427*(stop**5))-(0.18585*(stop**4))+((0.1465/3)*(stop**3))+(3.9335*(stop**2))+(5.721*stop))


def show_parts():
    print("Wspolczynnik przy x^5 :" + str(-0.00427))
    print("Wspolczynnik przy x^4 :" + str(-0.18585))
    print("Wspolczynnik przy x^3 :" + str(0.1465/3))
    print("Wspolczynnik przy x^2 :" + str(3.9335))
    print("Wspolczynnik przy x :" + str(5.721))


def func(x):
    return (-0.02135*(x**4))-(0.7434*(x**3))+(0.1465*(x**2))+(7.867*x)+5.721


def func_with_t(start,stop, t):
    x = (((stop+start) + (stop - start)*t))/2
    instead = (stop-start)/2
    return((-0.02135 * (x ** 4)) - (0.7434 * (x ** 3)) + (0.1465 * (x ** 2)) + (7.867 * x) + 5.721)*instead


def gauss_qadr(start,stop):
    return (5 / 9) * func_with_t(start, stop, -1*math.sqrt(3 / 5)) +\
           (8 / 9) * func_with_t(start, stop, 0) +\
           (5 / 9) * func_with_t(start, stop, math.sqrt(3 / 5))


def trapeze(start,stop, segments):
    suma = 0
    step = (stop-start)/segments
    for i in range(segments):
        a = func(start+(i*step))
        b = func(start+((i+1)*step))
        int = ((a+b)*step)/2
        suma += int
    return suma


def new_integral(given_list,index,step):
    return(4**(step)*given_list[index+1] - given_list[index])/((4**step)-1)


def richardson(given_list,steps):
    new_list = []
    new_list.append(given_list)
    error = 100
    for current_step in range (1,steps):
        current_list = []
        for i in range(0,len(new_list[current_step-1])-1):
            current_list.append(new_integral(new_list[current_step-1], i, current_step))
            error = (abs((current_list[-1] - new_list[-1][i+1])/current_list[-1])*100)
            if error<0.2:
                break
        new_list.append(current_list)
        if error < 0.2:
            break
    print(new_list)
    return error, new_list[-1][-1]

def romberg(start,stop, steps):
    first_step = []
    for i in range(steps):
        first_step.append(trapeze(start, stop, 2**(i+1)))
    error, result = richardson(first_step,steps)
    return error, result


integral = analitically(12, -32)
show_parts()
print("Analityczny wynik całki: " + str(integral))
error = 100
iterator = 2
result = 0
while error > 0.2:
    error, result = romberg(-32, 12, iterator)
    if error>0.2:
        iterator += 1
print("------------------------")
print("Metodą Romberga wynik = " + str(result))
print("Błąd względny wyniósł = " + str(error))
print("Osiągnięto dla n = " + str(iterator-1) + " kroków.")
gauss = gauss_qadr(-32,12)
print("------------------------")
print("Kwadratura Gaussa 3 punktowa wynik: " + str(gauss))