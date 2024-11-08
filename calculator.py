class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        # return b - a the numbers were swapped position
        return a - b

    def multiply(self, a, b):
        result = 0
        # for i in range(b+1):
        for i in range(b): # change b+1 to b
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        # add more: if divide by 0
        if b == 0:
            return "cannot devide by zero"
        # while a > b:
        while a >= b: # change a > b to a >= b
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        # while a <= b:
        while a >= b: # change a <= b to a >= b
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))