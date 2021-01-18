import tkinter
from tkinter import ttk
from yaml_test import write
from datetime import date



class add_new_data:


    def __init__(self,data_name):
        window = tkinter.Tk()
        window.title("add {0} - unsafe!!".format(data_name))

        today = date.today()

        tkinter.Label(window,text="data:").grid(column=0, row=0)
        data = tkinter.Entry(window, width=40)
        data.grid(column=1, row=0)
        data.insert(0,today)


        tkinter.Label(window, text="{0}:".format(data_name)).grid(column=0, row=1)
        value = tkinter.Entry(window, width=40)
        value.grid(column=1, row=1)

        tkinter.Label(window,text="comment:").grid(column=0, row=2)
        comment = tkinter.Entry(window, width=40)
        comment.grid(column=1, row=2)


        label_result = tkinter.Label(window, text="Result")
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




        tkinter.Button(window, text="add data", command=add_to_data).grid(column=0, row=6)




        window.mainloop()

