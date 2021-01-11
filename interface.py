'''
Simple GUI to display covid data
'''
import os
import tkinter
import show_graph
import test_graph_by_date
import dates_graph
import kcal_calculator


class interface:
    """
    cases/deaths
    day/month/all_days
    country/continent/world
    """


    def show_interface3(self):
        window = tkinter.Tk()
        window.title("Graphs")

        #Covdata = tkinter.Entry(window, width=40)
        #Covdata.grid(column=0, row=5)

        tkinter.Button(window, text="Show testing graph", command=show_graph.show_graph).grid(column=0, row=0)
        tkinter.Button(window, text="Show testing graph 2", command=test_graph_by_date.test_graph_by_date).grid(column=0, row=1)
        tkinter.Button(window, text="Show testing graph 3", command=dates_graph.dates_graph).grid(column=0, row=2)
        tkinter.Button(window, text="Calculate my kcal", command=kcal_calculator.kcal_calculator).grid(column=0, row=3)



        window.mainloop()

    def run(self):
        self.show_interface3()
