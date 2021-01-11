import tkinter

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class test_graph_by_date:

    def __init__(self):
        years = mdates.YearLocator()   # every year
        months = mdates.MonthLocator()  # every month
        years_fmt = mdates.DateFormatter('%Y')

        # Load a numpy structured array from yahoo csv data with fields date, open,
        # close, volume, adj_close from the mpl-data/example directory.  This array
        # stores the date as an np.datetime64 with a day unit ('D') in the 'date'
        # column.


        data = {
            'date': ["2008-10-30","2009-11-30"],
            'adj_close': [100,110]
        }

        data = cbook.get_sample_data('goog.npz', np_load=True)['price_data']

        fig, ax = plt.subplots()
        ax.plot('date', 'adj_close', data=data)

        # format the ticks
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(years_fmt)
        ax.xaxis.set_minor_locator(months)

        # round to nearest years.
        datemin = np.datetime64(data['date'][0], 'Y')
        datemax = np.datetime64(data['date'][-1], 'Y') + np.timedelta64(1, 'Y')
        #ax.set_xlim(datemin, datemax)

        # format the coords message box
        ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        ax.format_ydata = lambda x: '$%1.2f' % x  # format the price.
        ax.grid(True)

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


