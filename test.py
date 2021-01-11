from tkinter import *

from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


def raise_frame(frame):
    frame.tkraise()


def raise_graph():
    data = {
        1: 107,
        2: 108,
        3: 109
    }
    root2 = Tk()
    root2.wm_title("Wykres Wrzesień")

    fig = Figure(figsize=(5, 4), dpi=100)

    lists = sorted(data.items())  # sorted by key, return a list of tuples

    x, y = zip(*lists)  # unpack a list of pairs into two tuples

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x + b)

    fig.add_subplot(111).plot(x, y, color='green', linewidth=1, marker='o',linestyle='dashed', markerfacecolor='blue', markersize=6)
    fig.add_subplot(111).plot(x, m*x + b, color="orange")
    print(fig.__doc__)

    canvas = FigureCanvasTkAgg(fig, master=root2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


def raise_graph_2():
    x = np.array([1, 2, 3, 4, 5, 6, 7])
    y = np.array([68, 70, 75, 73, 63, 62, 63])
    labels = np.array(['pon', 'wt', 'śr', 'czw','pt','sob', 'nied'])

    root2 = Tk()
    root2.wm_title("My first apliacaction")

    #fig = Figure(figsize=(5, 4), dpi=100)
    fig, ax = plt.subplots(1, 1)

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b)
    plt.xticks(x, labels, rotation='vertical')
    fig.add_subplot(111).plot(x, y, color='green', linewidth=1, marker='o', linestyle='dashed', markerfacecolor='blue',
                              markersize=6)
    fig.add_subplot(111).plot(x, m * x + b, color="orange")
    ax.set_xticklabels(labels, rotation='vertical', fontsize=18)

    canvas = FigureCanvasTkAgg(fig, master=root2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

Button(f1, text='Go to frame 2', command=lambda:raise_graph_2()).pack()
Label(f1, text='FRAME 1').pack()

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()



