# Dylan Stitt
# Unit 4 Lab 4
# Balance Brackets

from Stack import ArrayStack

def check(brackets):
    stack = ArrayStack()
    for i in range(len(brackets)):
        stack.push(brackets[i])
    if len(stack) % 2 == 1:
        return "Unbalanced\n"

    stack = ArrayStack()
    for b in brackets:
        if b in ['(', '[', '{']:
            stack.push(b)
        else:
            br = None
            if b == ')': br = '('
            elif b == ']': br = '['
            else: br = '{'
            if stack.top() == br: stack.pop()

    if len(stack) % 2 == 0:
        return "Balanced\n"
    else:
        return "Unbalanced\n"

def main():
    test1 = "()(()){([()])}"
    test2 = "((()(()){([()])}))"
    test3 = ")(()){([()])]"
    test4 = "({[])}"
    test5 = "("

    for test in [test1, test2, test3, test4, test5]:
        b = check(test)
        print(test + f' - {b}')


if __name__ == '__main__':
    main()
