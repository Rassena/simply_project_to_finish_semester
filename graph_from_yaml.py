import tkinter


import matplotlib.pyplot as plt
from matplotlib.dates import (YEARLY, DateFormatter, rrulewrapper, RRuleLocator, drange)
import numpy as np
import datetime

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import yaml_test


class graph_from_yaml:

    def __init__(self,data_name):
        # tick every 5th easter
        rule = rrulewrapper(YEARLY, byeaster=1, interval=1)
        loc = RRuleLocator(rule)
        formatter = DateFormatter('%Y-%m-%d')
        date1 = datetime.date(2018, 1, 1)
        date2 = datetime.date(2021, 1, 12)
        delta = datetime.timedelta(days=7)

        dates_y = []
        values_y =[]

        data_from_yaml = yaml_test.get_yaml(data_name)
        for key, value in data_from_yaml.items():
            print("{0}: {1}: {2}; {3}".format(key, data_name, value.get(data_name),value.get('comment')))
            date = datetime.datetime.strptime(key,'%Y-%m-%d').date()
            print(date)
            dates_y = np.append(dates_y, date)
            values_y = np.append(values_y, (float) (value.get(data_name)))
            print(value.get(data_name))

        dates = drange(date1, date2, delta)
        s = np.random.rand(len(dates_y))  # make up some random y values


        fig, ax = plt.subplots()
        plt.plot_date(dates_y, values_y, color='green', linewidth=1, marker='o',linestyle='dashed', markerfacecolor='blue', markersize=6)
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

