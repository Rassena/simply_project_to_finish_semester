import matplotlib.pylab as plt
import numpy as np
import sqlite3 as sl

def Network():

    dict = {'CISCO' : 'NEXUS', 'JUNIPER' : 'JUNO', 'Alcatel' : 'Alc' }


    #len(dict)
    return (dict)



def db_store():
    con = sl.connect('my-test.db')

    sql = 'INSERT INTO test (date, weight) values(?, ?)'
    data = [
        (2020-10-1, 100),
        (2020-10-2, 99),
        (2020-10-3, 101)
    ]
    print(data)
    with con:
        con.executemany(sql, data)

    with con:
        con.executemany(sql, data)




d = {
        1: 107,
        2: 108,
        3: 109,
        4: 108
    }


lists = sorted(d.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

xn = np.asarray(x)
yn = np.asarray(y)

m, b = np.polyfit(xn, yn, 1)



plt.plot(x, y, color='green', linewidth=1, marker='o',linestyle='dashed', markerfacecolor='blue', markersize=6)
plt.plot(xn, m*xn + b, color="orange")
plt.show()

con = sl.connect('my-test.db')
data = [
    (2020 - 10 - 1, 100),
    (2020 - 10 - 2, 99),
    (2020 - 10 - 3, 101)
]
print(data)

sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
data = [
    (1, 'Alice', 21),
    (2, 'Bob', 22),
    (3, 'Chris', 23)
]

with con:
    con.executemany(sql, data)


with con:
    data = con.execute("SELECT * FROM USER WHERE age <= 22")
    for row in data:
        print(row)