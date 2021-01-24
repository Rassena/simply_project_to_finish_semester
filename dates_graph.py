import tkinter


import matplotlib.pyplot as plt
from matplotlib.dates import (YEARLY, DateFormatter, rrulewrapper, RRuleLocator, drange)
import numpy as np
import datetime

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class dates_graph:

    def __init__(self):
        # tick every 5th easter
        rule = rrulewrapper(YEARLY, byeaster=1, interval=1)
        loc = RRuleLocator(rule)
        formatter = DateFormatter('%Y-%m-%d')
        date1 = datetime.date(2018, 1, 1)
        date2 = datetime.date(2021, 1, 12)
        delta = datetime.timedelta(days=7)

        dates = drange(date1, date2, delta)
        s = np.random.rand(len(dates))  # make up some random y values


        fig, ax = plt.subplots()
        plt.plot_date(dates, s, color='green', linewidth=1, marker='o',linestyle='dashed', markerfacecolor='blue', markersize=6)
        #ax.xaxis.set_major_locator(loc)
        ax.xaxis.set_major_formatter(formatter)
        #ax.xaxis.set_tick_params(rotation=30, labelsize=10)

        root = tkinter.Tk()
        root.wm_title()

        f = Figure(figsize=(5, 4), dpi=100)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        # rotates and right aligns the x labels, and moves the bottom of the
        # axes up to make room for them
        fig.autofmt_xdate()

        tkinter.mainloop()


