class stack():
    def __init__(self):
        self.arr = []
    def push(self,element):
        self.arr.append(element)
    def pop(self):
        if self.size() != 0:
            return self.arr.pop()
    def size(self):
        return len(self.arr)
def reverse_string(s):
    str_stack = stack()
    reverse_str = ""
    for i in s:
        str_stack.push(i)
    while str_stack.size() != 0:
        reverse_str += str_stack.pop()
    return reverse_str