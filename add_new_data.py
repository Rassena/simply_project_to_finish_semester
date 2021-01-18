import tkinter
from tkinter import ttk
from yaml_test import write
from datetime import date



class add_new_data:


    def __init__(self,data_name):
        window_add = tkinter.Tk()
        window_add.title("add {0} - unsafe!!".format(data_name))

        today = date.today()

        tkinter.Label(window_add,text="data:").grid(column=0, row=0)
        data = tkinter.Entry(window_add, width=40)
        data.grid(column=1, row=0)
        data.insert(0,today)


        tkinter.Label(window_add, text="{0}:".format(data_name)).grid(column=0, row=1)
        value = tkinter.Entry(window_add, width=40)
        value.grid(column=1, row=1)

        tkinter.Label(window_add,text="comment:").grid(column=0, row=2)
        comment = tkinter.Entry(window_add, width=40)
        comment.grid(column=1, row=2)


        label_result = tkinter.Label(window_add, text="")
        label_result.grid(column=1, row=6)

        def add_to_data():
            label_result.config(text='dodano: {3} - {0}: {1}, comment: {2}'.format(data_name,value.get(),comment.get(),data.get()))

            new_yaml_data_dict = {
                data.get(): {
                    data_name: value.get(),
                    'comment': comment.get()
                }
            }
            write(new_yaml_data_dict, data_name)

        def exit():
            window_add.destroy()


        tkinter.Button(window_add, text="add data", command=add_to_data).grid(column=0, row=6)
        tkinter.Button(window_add, text="exit", command=exit).grid(column=0, row=7)



        window_add.mainloop()

