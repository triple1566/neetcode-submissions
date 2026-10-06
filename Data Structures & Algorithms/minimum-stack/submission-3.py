class MinStack:
    # **Constraints:**

    # `-2^31 <= val <= 2^31 - 1`.
    # `pop`, `top` and `getMin` will always be called on **non-empty** stacks.
    # At most 3∗1043∗104 calls will be made to `push`, `pop`, `top`, and `getMin`.


    # In our stack class, we also utilize stack to keep track of our minimum values

    def __init__(self):
        self.stackbody = []
        self.min = [float("inf")]

    def push(self, val: int) -> None:
        # Check if val is a new minimum
        if type(val) != int:
            return None
        elif self.min[-1] >= val:
            self.min.append(val)
        self.stackbody.append(val)
        return

    def pop(self) -> None:
        if self.top()==self.getMin():
            self.min.pop()
        self.stackbody.pop()


    def top(self) -> int:
        return self.stackbody[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
