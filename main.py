import tkinter

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import show_graph
from interface import interface
def archive():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 23, 24, 25, 27, 28, 30])
    y = np.array([68, 70, 75, 73, 63, 62, 63, 64, 68, 64, 67, 66, 65, 64, 67, 68, 64])


    X = np.arange(10, 100, 1)
    first = (X*2)**(X*2)
    second = ((X+1)*2)**((X+1)*2)
    Y = second -first

    root = tkinter.Tk()
    root.wm_title("My first apliacaction")

    fig = Figure(figsize=(5, 4), dpi=100)

    m, b = np.polyfit(x, y, 1)
    #plt.plot(x, m*x + b)
    plt.plot(X,Y)
    fig.add_subplot(111).plot(X, Y, color='green', linewidth=1, marker='o',linestyle='dashed', markerfacecolor='blue', markersize=6)
    #fig.add_subplot(111).plot(x, m*x + b, color="orange")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


    tkinter.mainloop()

intf = interface()
intf.run()