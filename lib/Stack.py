class Stack:

    def __init__(self, items = None, limit = 100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) == self.limit:
            print(f"Stack is already full!!")
            return
        self.items.append(item)
        print(f"{item} pushed to stack.")

    def pop(self):
        if self.isEmpty():
            print(f"Stack is empty no items to pop!!")
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            print(f"Stack is empty no items to peek!!")
            return None
        peek_item = self.items[-1]
        print(f"{peek_item} is the top on the stack.")
        return peek_item
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit
        
    def search(self, target):
        if target in self.items:
            index_of_target = self.items.index(target)
            index_of_top_item = len(self.items) - 1
            distance = index_of_top_item - index_of_target
            print(f"Distance is: {distance}")
            return distance
        else:
            print(f"{target} not found in the stack.")
            return -1
