big = lambda a,b,c: a if a>=b and a>c else b if b>=c and b>a else c if c>=a and c>b else 'all values are eual'

a,b,c = float(input('enter first value: ')),float(input('enter second value: ')),float(input('enter third value: '))
print('biggest value = ',big(a,b,c))