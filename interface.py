'''
Simple GUI to display covid data
'''
import os
import tkinter
import kcal_calculator
import add_new_data
from tkinter import ttk
from tkinter import *

import yaml_test
import graph_from_yaml

class interface:

    s_about = " Program ma na celu ułatwienia kontroli i podglądu postępów w wybranych \n " \
            "przez użytkownika czynnościach lub ćwiczeniach. \n" \
            "Wybrane zapisane dane mogą być wyświetlone za pomocą wykresu lub listy, która także zawiera komentarza. \n\n" \
            "Program Umożliwia obliczenie BMI i BMR z możliwością zapisania dla danego dnia. \n\n" \
            "Użytkownik także ma mozliwość stworzenia swojej własnej grupy danych. Dane te muszą mieć wartości liczbowe.\n\n" \
            "Ważne jest to żeby upewnić się przy dodawaniu nowych wartości, czy wybrana jest w liście grupa danych do których chce się dodać. \n" \
            "Także to istotne jest przy dodawania poprzez skróty klawiszowe \n\n" \
            "Program zapisuje dane za każdą dodaną nową wartością. Zagrożenie utraty danych jest prawdopodobne jedynie podczas zawieszenia się \n " \
            "prorgramu/systemu podczas zapisywynia (dodania) nowej wartości."

    arr = None
    select_graph =None

    def __init__(self):
        self.arr = os.listdir("data/")
        window = tkinter.Tk()
        window.title("Graphs")

        for i in range(len(self.arr)):
            self.arr[i] = self.arr[i].split('.')[0]

        def add_new_val():
            self.add_new_val(self)

        def add_new_group():
            self.add_new_group(self)


        def show_list():
            self.show_list(self)


        def show_graph_select():
            self.show_graph_select(self)


        def about():
            self.about(self)

        self.select_graph = ttk.Combobox(window, state="readonly", values=self.arr)
        self.select_graph.grid(column=0, row=0)
        self.select_graph.current(0)
        tkinter.Button(window, text="add new Value", command=add_new_val).grid(column=0, row=3)
        tkinter.Button(window, text="add new graph", command=add_new_group).grid(column=0, row=5)
        tkinter.Button(window, text="Show data list", command=show_list).grid(column=0, row=2)
        tkinter.Button(window, text="Show selected graph", command=show_graph_select).grid(column=0, row=1)
        tkinter.Button(window, text="Calculate my kcal", command=kcal_calculator.kcal_calculator).grid(column=0, row=4)
        tkinter.Button(window, text="exit", command=exit, fg="red").grid(column=0, row=6)

        menubar = Menu(window)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Group", command=add_new_group,accelerator="Ctrl+N")

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=exit,accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)


        editmenu.add_command(label="Open graph", command=show_graph_select,accelerator="Ctrl+G")
        editmenu.add_command(label="Open list", command=show_list,accelerator="Ctrl+L")
        editmenu.add_command(label="Add", command=add_new_val,accelerator="Ctrl+A")

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About...", command=about,accelerator="Ctrl+H")
        menubar.add_cascade(label="Help", menu=helpmenu)

        window.config(menu=menubar)
        window.bind('<Control-q>',self.exit)
        window.bind('<Control-n>',self.add_new_group)
        window.bind('<Control-h>',self.about)
        window.bind('<Control-l>', self.show_list)
        window.bind('<Control-a>', self.add_new_val)
        window.bind('<Control-g>', self.show_graph_select)



        window.mainloop()


    def run(self):
        self.__init__()



    """
    commands for shortcuts and other
    """

    def exit(self, event):
        exitsure = tkinter.Toplevel()

        areyousure = tkinter.Label(exitsure, text="Are you sure you want to exit?")
        areyousure.grid(column=0, row=0, columnspan=4)

        ExitYes = tkinter.Button(exitsure, text="Yes", fg="red", command=quit)
        ExitYes.grid(column=0, row=2)

        NoYes = tkinter.Button(exitsure, text="No", command=exitsure.destroy)
        NoYes.grid(column=2, row=2)

    def about(self, event):
        exitsure = tkinter.Toplevel()
        areyousure = tkinter.Label(exitsure, text=self.s_about)
        areyousure.grid(column=0, row=0, columnspan=3, rowspan=3)

        ok = tkinter.Button(exitsure, text="Ok", command=exitsure.destroy)
        ok.grid(column=1, row=10)


    def add_new_val(self, event):
        add_new_data.add_new_data(self.select_graph.get())

    def add_new_group(self, event):
        def new_group():
            if not os.path.isfile("data/{0}.yaml".format(value.get())):
                with open("data/{0}.yaml".format(value.get()), "a") as fo:
                    fo.write("---\n")
                for i in range(len(self.arr)):
                    self.arr[i] = self.arr[i].split('.')[0]
                self.updtcblist()
                exit_add_group()
            else:
                label_result.config(text='{0} already exist'.format(value.get()))

        def exit_add_group():
            exitsure = tkinter.Toplevel()

            areyousure = tkinter.Label(exitsure, text="Are you sure you want to exit?")
            areyousure.grid(column=0, row=0, columnspan=4)

            ExitYes = tkinter.Button(exitsure, text="Yes", fg="red",
                                     command=lambda: [window_a.destroy(), exitsure.destroy()])
            ExitYes.grid(column=0, row=2)

            NoYes = tkinter.Button(exitsure, text="No", command=exitsure.destroy)
            NoYes.grid(column=2, row=2)

        window_a = tkinter.Tk()
        tkinter.Label(window_a, text="Name of new group").grid(column=0, row=0)
        value = tkinter.Entry(window_a, width=40)
        value.grid(column=1, row=0)

        tkinter.Button(window_a, text="Add", command=new_group).grid(column=0, row=1)
        tkinter.Button(window_a, text="exit", command=exit_add_group).grid(column=0, row=2)

        label_result = tkinter.Label(window_a, text="")
        label_result.grid(column=1, row=1)

    def show_list(self, event):
        def exit():
            exitsure = tkinter.Toplevel()

            areyousure = tkinter.Label(exitsure, text="Are you sure you want to exit?")
            areyousure.grid(column=0, row=0, columnspan=4)

            ExitYes = tkinter.Button(exitsure, text="Yes", fg="red",
                                     command=lambda: [window_s.destroy(), exitsure.destroy()])
            ExitYes.grid(column=0, row=2)

            NoYes = tkinter.Button(exitsure, text="No", command=exitsure.destroy)
            NoYes.grid(column=2, row=2)

        window_s = tkinter.Tk()
        window_s.title("Graphs")

        data_from_yaml = yaml_test.get_yaml(self.select_graph.get())

        for key in sorted(data_from_yaml):
            print(key, data_from_yaml[key].get(self.select_graph.get()), data_from_yaml[key].get('comment'))


        if data_from_yaml is not None:

            my_list = tkinter.Listbox(window_s)
            my_list.grid(column=0, row=0)

            for key, value in data_from_yaml.items():
                my_list.insert(tkinter.END,
                               "{0}: {1}: {2}; {3}".format(key, self.select_graph.get(), value.get(self.select_graph.get()),
                                                           value.get('comment')))

            my_list.config(width=100)

        else:
            label_result = tkinter.Label(window_s, text="No data to show")
            label_result.grid(column=0, row=0)

        tkinter.Button(window_s, text="exit", command=exit, fg="red").grid(column=0, row=1)
        window_s.mainloop()

    def updtcblist(self):
        arr = os.listdir("data/")
        for i in range(len(arr)):
            arr[i] = arr[i].split('.')[0]
        self.select_graph.configure(value=self.arr)

    def show_graph_select(self, event):
        graph_from_yaml.graph_from_yaml(self.select_graph.get())

        def donothing(self, event):
            filewin = Toplevel(self)
            button = Button(filewin, text="Do nothing button")
            button.pack()