# Импорт библиотек numpy и matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Объявление исходной функции
def f(x):
    return x - 5 * np.log(x)

# Алгоритм метода хорд
def hord(a, b, eps):
    def fx(a1, b1):
        # Определение длины хорды по текущим значениям а и b
        return (b1 - a1) / (f(b1) - f(a1))

    n = 0  # Инициализация счетчика итераций
    # Цикл выполнения метода, пока разница между а и b не достигнет заданного значения epsilon
    while abs(a - b) > eps:
        a = b - f(b) * fx(a, b)
        b = a - f(a) * fx(a, b)
        n = n + 1  # увеличиваем счетчик итераций на 1 каждую итерацию
    return [(a + b) / 2, n]

# Алгоритм метода секущих
def secant(a, b, eps):
    x2 = a
    x1 = b
    n = 0  # Инициализация счетчика итераций
    # Цикл выполнения метода, пока разница между а и b не достигнет заданного значения epsilon
    while abs(x2 - x1) > eps:
        x0 = x1
        x1 = x2
        x2 = x1 - ((x0 - x1) * f(x1)) / (f(x0) - f(x1))
        n = n + 1  # увеличиваем счетчик итераций на 1 каждую итерацию
    return [x2, n]

# Алгоритм метода итераций с переориентацией от a к b
def iterativeMethod(a, b, eps):
    n = 0 # Инициализация счетчика итераций
    x = a  # Инициализация значения x
    # Цикл выполнения метода, пока разница между а и b не достигнет заданного значения epsilon
    while abs(a - b) > eps:
        x = a + 0.25*(a-5*np.log(a)) # Следующее приближение x
        a = b
        b = x
        n += 1 # увеличиваем счетчик итераций на 1 каждую итерацию
    return [x, n]

# Алгоритм "Метод отделения корней", чтобы найти интервалы с корнями функции
def rootSeparation(x0, x1, deltax):
    x = x0 # начало интервала
    y0 = f(x)
    m = 0 # счётчик корней
    x = x + deltax # делаем шаг
    while x <= x1:
        y1 = f(x)
        # если есть корень между y0 и y1
        if y0 * y1 <= 0:
            m = m + 1 # увеличиваем счётчик корней
            b = x
            a = b - deltax
            print([m, a, b]) # печатаем пару значений a и b
        y0 = y1
        x = x + deltax
    return ""

# набор значения epsilon для сравнения скорости сходимости различных методов
eps2 = [0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]

# Далее следует блок вывода результатов работы методов и построения графиков
print("Метод отделения корней")
print(rootSeparation(0.1, 15, 0.01))
print("Метод хорд")
print("Интервал от 1.29 до 1.3")
for i in eps2:
    print(hord(1.29, 1.3, i))
print()
print("Метод секущих")
print("Интервал от 1.29 до 1.3")
for i in eps2:
    print(secant(1.29, 1.3, i))
print()
print("Метод итераций")
print("Интервал от 1.29 до 1.3")
for i in eps2:
    print(iterativeMethod(1.29, 1.3, i))
print()
print("Метод обратных итераций")
print("Интервал от 1.29 до 1.3")
for i in eps2:
    print(iterativeMethod(1.3, 1.29, i))
print()

# Представлены функции (chart1, chart2, chart3, chart4) для построения графиков функции и результатов работы методов.
# график функции на интервале от -10 до 10
def chart1():
    x = np.arange(0.1, 15, 0.01)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, color='red')
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid()
    ax.set_title("График функции на интервале от -10 до 10")
    plt.ylim([-4.5, 10])
    plt.show()

# график функций на малом интервале для 1 корня
def chart2():
    x = np.arange(1.2, 1.3, 0.01)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, color='red')
    ax.axhline(0, color='black', linewidth=1)
    #ax.axvline(0, color='black', linewidth=1)
    ax.grid()
    ax.set_title("График корня")
    plt.show()

eps = 10**np.linspace(-1,-7,100)
# Используется функция axisY для получения количества итераций для каждого метода с разными значениями epsilon.
def axisY(a, b, method):
    y = [method(a, b, e)[1] for e in eps]
    return y

def chart3():
    plt.figure()
    plt.title('График временных затрат на интервале [1.29, 1.3]')
    plt.xscale('log')
    plt.step(eps, axisY(1.29, 1.3, hord), 'r-', label='Метод хорд')
    plt.step(eps, axisY(1.29, 1.3, secant), 'b-', label='Метод секущих')
    plt.step(eps, axisY(1.29, 1.3, iterativeMethod), 'y-', label='Метод итераций а до b')
    plt.step(eps, axisY(1.3, 1.29, iterativeMethod), 'g-', label='Метод итераций b до а')
    plt.legend(['Метод хорд', 'Метод секущих', 'Метод итераций а до b', 'Метод обратных итераций b до а'])
    plt.grid()
    plt.show()

def chart4():
    plt.figure()
    plt.title('График временных затрат на интервале [0.01, 10]')
    plt.xscale('log')
    plt.step(eps, axisY(0.01, 10, hord), 'r-', label='Метод хорд')
    plt.step(eps, axisY(0.01, 10, secant), 'b-', label='Метод секущих')
    plt.step(eps, axisY(0.01, 10, iterativeMethod), 'y-', label='Метод итераций а до b')
    plt.step(eps, axisY(10, 0.01, iterativeMethod), 'g-', label='Метод итераций b до а')
    plt.legend(['Метод хорд', 'Метод секущих', 'Метод итераций а до b', 'Метод итераций b до а'])
    plt.grid()
    plt.show()


chart1()
chart2()
chart3()
chart4()

