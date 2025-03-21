'''''''''
# 1 вариант решения
skobki = input()
stack = []
is_good = True
for i in skobki:
     
    if i in '({[':
        stack.append(i)
    elif i in "]})":
        if not stack:
            is_good = False
            break
        open_bracket = stack.pop()
        if open_bracket == '(' and i == ')':
            continue
        if open_bracket == '{' and i == '}':
            continue
        if open_bracket == '[' and i == ']':
            continue
        is_good = False
        break

if is_good and len(stack)==0:
    print('YES')
else:
    print('NO')
    
'''''''''''


#Вариант 2

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
    


skob = input()
stacks = Stack()
is_good = True

for i in skob:
    if i in '({[':
        stacks.push(i)

    if i in ')}]':
        if stacks.is_empty() == True:
            is_good = False
            break

        obg = stacks.peek()
        stacks.pop()
        if obg == '(' and i == ')':
            continue
        if obg == '{' and i == '}':
            continue
        if obg == '[' and i == ']':
            continue
        is_good = False
        break
        
if is_good and stacks.is_empty() == True:
    print('YES')
else:
    print('NO')

