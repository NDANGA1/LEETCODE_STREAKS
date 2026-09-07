
def evalRPN(tokens):
    stack = []
    res = 0
    for t in tokens:
        if t in ('+', '-', '*', '/'):
            while stack:
                if t == '+':
                    res += stack.pop()
                elif t == '-':
                    res -= stack.pop()
                elif t == '*':
                    res *= stack.pop()
                else:
                    res /= stack.pop()
            stack.append(res)
            print(res)
        else:
            stack.append(int(t))
        print(stack)
        print(t)
        print(".................................")
        print(".................................")

    return stack.pop()

print(evalRPN(["2","1","+","3","*"]))
