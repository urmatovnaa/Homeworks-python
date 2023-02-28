class Todo:
    def __init__(self):
        self.todo_items = []

    def add_todo(self, item):
        if not isinstance(item, TodoItem):
            return
        self.todo_items.append(item)

    def list_items(self):
        q = 1
        for i in self.todo_items:
            print(f'{q}, {i}')
            q += 1

    def find(self, word):
        name_list = []
        for i, v in enumerate(self.todo_items):
            if word in v.task:
                name_list.append(f'{i+1}: {v}')
        return name_list


class TodoItem:
    def __init__(self, task):
        self.__task = task
        self.__is_done = False

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, task):
        self.__task = task

    def check(self):
        if self.__is_done:
            self.__is_done = False
        else:
            self.__is_done = True

    def __repr__(self):
        return self.task
