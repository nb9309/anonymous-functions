ad = lambda a,b:a+b
sub = lambda a,b:a-b
mul = lambda a,b:a*b
div = lambda a,b:a/b
fd = lambda a,b:a//b
mod = lambda a,b:a%b
exp = lambda a,b:a**b

a = float(input())
b = float(input())

while 9:
    n = input('enter operator: ')
    if n not in('+','-','*','/','//','**','%'):
        break
    else:
        match(n):
            case '+':
                print('{}+{}={}'.format(a,b,ad(a,b)))
            case '-':
                print('{}-{}={}'.format(a, b, sub(a, b)))
            case '*':
                print('{}*{}={}'.format(a, b, mul(a, b)))
            case '/':
                print('{}/{}={}'.format(a, b, div(a, b)))
            case '//':
                print('{}//{}={}'.format(a, b, fd(a, b)))
            case '%':
                print('{}%{}={}'.format(a, b, mod(a, b)))
            case '**':
                print('{}**{}={}'.format(a, b, exp(a, b)))
            case _:
                print('input is invalid')