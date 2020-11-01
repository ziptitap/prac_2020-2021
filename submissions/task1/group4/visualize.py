import numpy as np 
import matplotlib.pyplot as plt

def draw_graph(values, color, num):
    num += 1
    for i in range(values.shape[0]):
        print("%.2f" % (values[i]), end = '  ')
    
    fig, ax = plt.subplots()
    
    plt.ylim (0, np.amax(values)+1)
    plt.title("Визуализация спектров оптимальных стратегий", color = color) # заголовок
    plt.xlabel("Спектр оптимальной стратегии", color = color)# ось абсцисс
    plt.ylabel("Значения спектра", color = color)# ось ординат
    (markerline, stemlines, baseline) = plt.stem(values)#use_line_collection=True - добавлять, если не работает
    plt.minorticks_on()
    plt.setp(baseline, visible=False)
    plt.show()
    fig.savefig('мой график{}.pdf'.format(num))