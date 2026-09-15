class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        #push element, update minimum
        self.mainStack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        

        

    def pop(self) -> None:
        #pop element, check if minimum is removed
        val = self.mainStack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        #return most recent element added
        if self.mainStack:
            return self.mainStack[-1]
        else:
            return None
        

    def getMin(self) -> int:
        #return minimum element in stack
        
        return self.minStack[-1]
        
        
