import tkinter

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class show_graph:

    def __init__(self):
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 23, 24, 25, 27, 28, 30])
        y = np.array([68, 70, 75, 73, 63, 62, 63, 64, 68, 64, 67, 66, 65, 64, 67, 68, 64])

        data = {
            1: 107,
            2: 108,
            3: 109
        }
        root = tkinter.Tk()
        root.wm_title("to jest test")

        fig = Figure(figsize=(5, 4), dpi=100)

        m, b = np.polyfit(x, y, 1)
        plt.plot(x, m*x + b)
        plt.plot(x,y)
        fig.add_subplot(111).plot(x,y, color='green', linewidth=1, marker='o',linestyle='dashed', markerfacecolor='blue', markersize=6)
        fig.add_subplot(111).plot(x, m*x + b, color="orange")

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        tkinter.mainloop()



