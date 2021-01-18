"""
For men: BMR = 10 x weight (kg) + 6.25 x height (cm) – 5 x age (years) + 5

For women: BMR = 10 x weight (kg) + 6.25 x height (cm) – 5 x age (years) – 161


Sedentary (little or no exercise) : Calorie-Calculation = BMR x 1.2
Lightly active (light exercise/sports 1-3 days/week) : Calorie-Calculation = BMR x 1.375
Moderately active (moderate exercise/sports 3-5 days/week) : Calorie-Calculation = BMR x 1.55
Very active (hard exercise/sports 6-7 days a week) : Calorie-Calculation = BMR x 1.725
If you are extra active (very hard exercise/sports & a physical job) : Calorie-Calculation = BMR x 1.9

"""

import tkinter
from tkinter import ttk
import yaml_test



class kcal_calculator:


    def __init__(self):
        window = tkinter.Tk()
        window.title("simple kcal calculator !!unsafe!!")

        data_user_y = yaml_test.get_user()

        tkinter.Label(window,text="height (cm):").grid(column=0, row=0)
        height = tkinter.Entry(window, width=40)
        height.grid(column=1, row=0)


        tkinter.Label(window, text="weight (kg):").grid(column=0, row=1)
        weight = tkinter.Entry(window, width=40)
        weight.grid(column=1, row=1)

        tkinter.Label(window, text="age (years):").grid(column=0, row=2)
        age = tkinter.Entry(window, width=40)
        age.grid(column=1, row=2)

        sex= ttk.Combobox(window, width=35,state="readonly",values=["Men","Women"])
        sex.grid(column=1, row=3)
        sex.current(0)


        activity = ttk.Combobox(window, width=35,state="readonly",values=[
            "Little or no exercise",
            "Light exercise 1-3 days/week",
            "Moderate exercise 3-5 days/week",
            "Hard exercise 6-7 days a week",
            "Very hard exercise & a physical job"
                                               ])
        activity.grid(column=1, row=4)
        activity.current(0)


        label_result = tkinter.Label(window, text="Result")
        label_result.grid(column=1, row=6)

        def calculate():

            switch_activity = {0: 1.2,1: 1.375,2: 1.55,3:  1.725,4: 1.9}

            switch_sex = {0: 5,1: -161}

            height_a = int(height.get())
            weight_a = int(weight.get())
            age_a = int(age.get())

            result = 10* weight_a + 6.25* height_a - 5*age_a + switch_sex.get(sex.current())
            result*= switch_activity.get(activity.current())

            label_result.config(text='{0} kcal/day for {1} '.format(result,sex.get()))

            user_data = {
                'height': height_a,
                'weight': weight_a,
                'age': age_a,
                'activity':activity.current(),
                'sex': sex.current(),
            }
            yaml_test.user(user_data)
            print(user_data)


        def exit():
            window.destroy()

        tkinter.Button(window, text="Calculate my kcal", command=calculate).grid(column=0, row=6)
        tkinter.Button(window, text="exit", command=exit).grid(column=0, row=7)


        height.insert(0,data_user_y.get('height'))
        weight.insert(0,data_user_y.get('weight'))
        age.insert(0,data_user_y.get('age'))
        activity.current(data_user_y.get('activity'))
        sex.current(data_user_y.get('sex'))



        window.mainloop()

