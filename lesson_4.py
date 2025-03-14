#Шаг 1: Создание класса Stack

class Stack:
    def __init__(self):
        self.items = []

    #Шаг 2: Метод is_empty

    def is_empty(self):
        return len(self.items) == 0
    
    #Метод push

    def push(self, item):
        self.items.append(item)

    #Шаг 4: Метод pop
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")
        
    # Шаг 5: Метод peek
    def peek(self):
        if not self.is_empty():
            return self.items[1]
        else:
            raise IndexError("Стек пуст")
        
    #Метод size
    def size(self):
        return len(self.items)
    

my_stack = Stack()

my_stack.push(5)
my_stack.push(10)
my_stack.push(15)
my_stack.push(20)


print("Вершина стека:", my_stack.peek())

my_stack.pop()

print("Стек пуст?", my_stack.is_empty())

print("Размер стека:", my_stack.size())
