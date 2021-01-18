'''
Simple GUI to display covid data
'''
import os
import tkinter
import show_graph
import test_graph_by_date
import dates_graph
import kcal_calculator
import add_new_data
from tkinter import ttk
import yaml_test
import graph_from_yaml

class interface:
    """
    cases/deaths
    day/month/all_days
    country/continent/world
    """




    def show_interface3(self):
        arr = os.listdir("data/")
        window = tkinter.Tk()
        window.title("Graphs")


        for i in range(len(arr)):
            arr[i] = arr[i].split('.')[0]

        def add_new_val():
            add_new_data.add_new_data(select_graph.get())

        def add_new_group():
            def new_group():
                if not os.path.isfile("data/{0}.yaml".format(value.get())):
                    with open("data/{0}.yaml".format(value.get()), "a") as fo:
                        fo.write("---\n")
                    for i in range(len(arr)):
                        arr[i] = arr[i].split('.')[0]
                    updtcblist()
                    exit_add_group()
                else:
                    label_result.config(text='{0} already exist'.format(value.get()))

            def exit_add_group():
                window_a.destroy()

            window_a = tkinter.Tk()
            tkinter.Label(window_a, text="Name of new group").grid(column=0, row=0)
            value = tkinter.Entry(window_a, width=40)
            value.grid(column=1, row=0)

            tkinter.Button(window_a, text="Add", command=new_group).grid(column=0, row=1)
            tkinter.Button(window_a, text="exit", command=exit_add_group).grid(column=0, row=2)

            label_result = tkinter.Label(window_a, text="")
            label_result.grid(column=1, row=1)


        def show_list():
            def exit():
                    window_s.destroy()

            window_s = tkinter.Tk()
            my_list = tkinter.Listbox(window_s)
            my_list.grid(column=0, row=0)


            data_from_yaml = yaml_test.get_yaml(select_graph.get())
            for key, value in data_from_yaml.items():
                    my_list.insert(tkinter.END,"{0}: {1}: {2}; {3}".format(key,select_graph.get(),value.get(select_graph.get()),value.get('comment')))

            tkinter.Button(window_s, text="exit", command=exit).grid(column=0, row=1)
            label_result = tkinter.Label(window_s, text="")
            label_result.grid(column=1, row=1)
            my_list.config(width=100)
            window_s.mainloop()

        def updtcblist():
            arr = os.listdir("data/")
            for i in range(len(arr)):
                arr[i] = arr[i].split('.')[0]
            select_graph.configure(value=arr)

        def show_graph_select():
            graph_from_yaml.graph_from_yaml(select_graph.get())

        def exit():
            window.quit()

        #tkinter.Button(window, text="Show testing graph", command=show_graph.show_graph).grid(column=0, row=0)
        #tkinter.Button(window, text="Show testing graph 2", command=test_graph_by_date.test_graph_by_date).grid(column=0, row=1)
        #tkinter.Button(window, text="Show testing graph 3", command=dates_graph.dates_graph).grid(column=0, row=2)



        select_graph = ttk.Combobox(window, state="readonly", values=arr)
        select_graph.grid(column=0, row=0)
        select_graph.current(0)
        tkinter.Button(window, text="add new Value", command=add_new_val).grid(column=0, row=3)
        tkinter.Button(window, text="add new graph", command=add_new_group).grid(column=0, row=5)
        tkinter.Button(window, text="Show data list", command=show_list).grid(column=0, row=2)
        tkinter.Button(window, text="Show selected graph", command=show_graph_select).grid(column=0, row=1)
        tkinter.Button(window, text="Calculate my kcal", command=kcal_calculator.kcal_calculator).grid(column=0, row=4)
        tkinter.Button(window, text="exit", command=exit).grid(column=0, row=6)




        window.mainloop()




    def run(self):
        self.show_interface3()
