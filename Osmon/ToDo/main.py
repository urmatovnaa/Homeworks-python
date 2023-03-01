from models import Todo, TodoItem


def main():
    my_todo = Todo()

    for i in range(1_000_000):
        print("'+' - Добавить запись\n'f' - Поиск записи\n'q' - Выход из проги")
        user_in = input('Введите команду: ')

        if user_in == '+':
            my_task = TodoItem(input('Добавить запись: '))
            my_todo.add_todo(my_task)
            my_todo.list_items()

        elif user_in == 'f':
            lst = my_todo.find(input('Поиск: '))
            if lst == []:
                print('Такой записи нет')
            else:
                print(lst)

        elif user_in == 'q':
            break

        else:
            print('Неизвестная команда')


if __name__ == '__main__':
    main()
