class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    # Write your code here
    if not self.is_full():
            self.top+=1
            self.items[self.top]=data
  def pop(self) -> None:
    # Write your code here 
   if not self.is_empty():
            x=self.items[self.top]
            self.top-=1

  def status(self):
    """
    It prints all the elements of stack.
    """
    # Write your code here  
    for i in range(self.top+1):
            print(self.items[i]) 


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
