
class DoubleExpression:
    def __init__(self, value):
        self.value = value

    def print(self, buffer):
        buffer.append(str(self.value))    

    def eval(self): return self.value    

class AdditionalExpression:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')

    def eval(self):
        return self.left.eval() + self.right.eval()

if __name__ == '__main__':
    # 1 + (2+3)
    e = AdditionalExpression(
        DoubleExpression(1),
        AdditionalExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    e.print(buffer)
    print(''.join(buffer), ' = ', e.eval())
