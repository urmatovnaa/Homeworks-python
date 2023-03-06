import sqlite3
from pprint import pprint

conn = sqlite3.connect('example.db')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE employees
             (employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
              first_name TEXT,
              last_name TEXT,
              department TEXT,
              salary REAL)''')
except:
    pass
while True:
    print("Меню:")
    print("Посмотреть таблицу сотрудников:")
    answer = input("Yes\ No").lower()
    if answer == 'no':
        break
    elif answer == "yes":
        print("Хотите отсортировать ?")
        answer_1 = input("Yes\ No").lower()
        if answer_1 == 'no':
            pass
        elif answer_1 == 'yes':
            answer_2 = input('Введите поле по которому будет происходить сортировка(Укажите с минусом чтобы отсортировать в обратном порядке)').lower()
            if '-' in answer_2:
                c.execute(F"SELECT * FROM employees ORDER BY {answer_2[1:]} DESK")
            else:
                c.execute(F"SELECT * FROM employees ORDER BY {answer_2} ")
                pprint(c.fetchall())
        answer_3 = input("Хотите получить определенные поля? YES\ NO").lower()
        if answer_3 == 'no':
            c.execute('SELECT * FROM employees')
            pprint(c.fetchall())
        elif answer_3 == 'yes':
            a = input('Введите поля через запятую')
            c.execute(f'SELECT {a} FROM employees')
            pprint(c.fetchall())








# c.execute("""SELECT first_name, last_name FROM employees WHERE salary > 5000;""")
# pprint(c.fetchall())
# print("---"*10)
#
# c.execute("SELECT first_name, last_name, salary FROM employees")
# pprint(c.fetchall())
#
# c.execute("INSERT INTO employees(first_name, last_name, salary) VALUES ('Oscar','De Lahoya','200000'),('Mike','Tayson','30000')")



conn.commit()