class Stack:
    # список для хранения элементов стека.
    def __init__(self):
        self.items = []

    def is_empty(self):
        #  который будет проверять, пуст ли стек.
        return len(self.items) == 0

    def push(self, item):
        # который будет добавлять элемент в стек. Мы будем добавлять элемент в конец списка
        self.items.append(item)

    def pop(self):
        #  который будет удалять и возвращать элемент из вершины стека. При этом мы проверим, не пуст ли стек перед попыткой извлечения элемента.
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        #  который будет возвращать элемент из вершины стека без его удаления. Также проверим, не пуст ли стек перед попыткой просмотра элемента.
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def size(self):
        #который будет возвращать количество элементов в стеке.
        return len(self.items)
    
    # Создаем экземпляр стека
my_stack = Stack()

# Добавляем элементы в стек
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

# Просматриваем вершину стека
print("Вершина стека:", my_stack.peek())

# Удаляем элемент из стека
my_stack.pop()

# Проверяем, пуст ли стек
print("Стек пуст?", my_stack.is_empty())

# Выводим размер стека
print("Размер стека:", my_stack.size())
