# || =====\\ Stack is a Restricted Data Structure (Stack Implemented by Array is Static, But Stack Implemented by Linked List is Dynamic Data Structure) //===== ||

# || In Stack, Data items are inserted and deleted at One End Only || Stack follows LIFO(Last In First Out) & FILO(First In Last Out) Concept || Stack is a Restricted Data Structure ||
# || In Stack, Adding an item is called Push & Removing is called Pop || While Push, At First, We need to check the Overflow Condition & While Pop, we need to check the Underflow Condition ||
# || If Stack is full, Then it is Said to be an Overflow Condition & On the other hand, if Stack is Empty, Then it is said to be an Underflow Condition ||

# || 01 ||
class Stack:
    max_size = 3

    def __init__(self):
        self.items = []
    
    def __repr__(self):
        return repr(self.items)

    def push(self, item): # Constant Time Complexity O(1)
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            print("Stack Overflow!")

    def pop(self): # Constant Time Complexity O(1) 
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return print("Stack Underflow!")

    def is_empty(self): # Constant Time Complexity O(1)
        if not self.items:
            return True
        else:
            return False
s = Stack()
s.push(10)
s.push(20)
s.push(30)
# print(s.isempty())
print(s) 

# || Tower of Hanoi - Concept in Stack ||
    # Not Created right now

# || Infix, Prefix is also called Polish Notation, Postfix is also called Reverse Polish Notation - Expressions are used in Stack ||

# || Infix to Postfix Expression Conversting Function ||
def infix_to_postfix(expression):
    precedence = {}
    precedence["/"] = 2
    precedence["*"] = 2
    precedence["-"] = 1
    precedence["+"] = 1
    
    operators = Stack()
    postfix = []

    for item in expression:
        if item.isdigit():
            postfix.append(item)
        elif item in "*/-+":
            while operators.is_empty() is False:
                op = operators.pop()
                if precedence[op] >= precedence[item]:
                    postfix.append(op)
                else:
                    operators.push(op)
                    break
            operators.push(item)
    while operators.is_empty() is False:
        op = operators.pop()
        postfix.append(op)
    return " ".join(postfix)
infix_expression = "1 + 2 + 3 * 4 - 5"
postfix_expression = infix_to_postfix(infix_expression)
print(f"Infix Expression : {infix_expression}\nPostfix  Expression : {postfix_expression}")

# || Postfix Evaluating Function || 01 ||
def do_operation(operand1, operand2, operator):
    return eval(operand1 + operator + operand2)

def postfix_evaluate(expression):
    operands =[]
    operators = "*/-+"
    for character in expression:
        if character.isdigit():
            operands.append(character)
        elif character in operators:
            operand1 = operands.pop()
            operand2 = operands.pop()
            result = do_operation(operand1, operand2, character)
            operands.append(str(result))
    result = operands.pop()
    return result
print(postfix_evaluate(postfix_expression))

# || Postfix Evaluating Function || 02 ||
def postfix_evaluate(expression):
    operands = []
    operators = ["*", "/", "-","+"]
    expression_list = expression.split(",")
    for item in expression_list:
        if item in operators:
            operand1 = operands.pop()
            operand2 = operands.pop()
            result = do_operation(operand1, operand2, item)
            operands.append(str(result))
        else:
            operands.append(item)
    result = operands.pop()
    return result
expression = "20,30,+,2,*,10,*,4,/"
print(postfix_evaluate(expression))
