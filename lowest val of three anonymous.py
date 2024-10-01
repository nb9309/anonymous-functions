low = lambda a,b,c: a if a<=b and a<c else b if b<=c and b<c else c if c<=a and c<b else 'all are equal'

a,b,c = float(input('enter first value: ')),float(input('enter second value: ')),float(input('enter third value: '))
print('lowesr number is ',low(a,b,c))