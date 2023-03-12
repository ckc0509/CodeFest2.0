def toPostfix(words):
    precedence = {'/':2,'*':2,'+':1,'-':1}
    stack = []
    postfix = []
    for i in words:
        if precedence.get(i) == None:
            postfix.append(i)
        else:
            if not stack or precedence.get(i) > precedence.get(stack[-1]):
                stack.append(i)
            else:
                while stack and precedence.get(i) <= precedence.get(stack[-1]):
                    postfix.append(stack.pop())
                stack.append(i)
    while stack:
        postfix.append(stack.pop())
    return postfix
    
def evaluateExpr(expr):
    expr = toPostfix(expr)
    stack = []
    for i in expr:
        if str(i) not in '/*-+':
            stack.append(i)
        else:
            x = stack.pop()
            y = stack.pop()
            if i == '/':
                stack.append(y/x)
            elif i == '*':
                stack.append(y*x)
            elif i == '-':
                stack.append(y-x)
            elif i == '+':
                stack.append(y+x)
    ans = stack.pop()
    if isinstance(ans,float) and ans.is_integer():
        return int(ans)
    else:
        return ans
        
def wordToNumber(lst):
    s = []
    num = 0
    numbermapping = {'one':1,'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,
               'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19,
               'ten':10, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90}
    operatormapping = {'plus':'+', 'substract':'-', 'multiple':'*', 'division':'/',
                        '+':'+', '-':'-', '*':'*', '/':'/'}
    for i in lst:
        if i == 'and':
            continue
        if operatormapping.get(i) == None:
            if i == 'hundred':
                num *= 100
            else:
                if numbermapping.get(i) == None:
                    num += int(i)
                else:
                    num += numbermapping.get(i)
        else:
            s.append(num)
            s.append(operatormapping.get(i))
            num = 0
    s.append(num)
    return s

#driver code

with open("TMW_large.txt","r") as ip, open("output.txt","w") as op:
    N = int(ip.readline())
    case = 1
    for _ in range(N):
        expr = list(ip.readline().split())
        givenAns = float(expr[-1])
        if givenAns.is_integer():
            givenAns = int(givenAns)
        expr = expr[:-2]
        expr = wordToNumber(expr)
        actualAns = evaluateExpr(expr)
        #print(actualAns,givenAns)
        if actualAns == givenAns:
            op.write("Case #" + str(case) + ": true\n")
        else:
            op.write("Case #" + str(case) + ": false\n")
        case += 1