big = lambda a,b: a if a>b else b if b>a else 'both are equal'
a,b= float(input('enter first value: ')),float(input('enter second value: '))

if big(a,b) == a:
    print(f'{a} > {b}')
elif big(a,b) == b:
    print('{} > {}'.format(b,a))
else:
    print('{},{} both are equal'.format(a,b))