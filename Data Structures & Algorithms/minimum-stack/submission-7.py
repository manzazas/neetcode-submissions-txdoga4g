class MinStack:

    def __init__(self):
        self.arr = []
        self.min_stack = []
        
        

        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.min_stack:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)
            
        

    def pop(self) -> None:
        if self.arr[-1] == self.min_stack[-1]:
            self.min_stack.pop()
           
        
        self.arr.pop()
        
        

    def top(self) -> int:
        return self.arr[-1]

        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1
        
