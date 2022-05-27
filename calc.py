print('welcome to calculator.')
calculate = input('How would you like to calculate? (add,subtract,multiply,divide or exponet)')
if calculate == 'multiply':
    print('you selected multiply. choose numbers to multiply')
    x = int(input())
    y = int(input())
    print(x * y)

if calculate == 'add':
    print('you selected add. choose numbers to add')
    z = int(input())
    a = int(input())
    print(z + a)

if calculate == 'subtract':
    print('you selected subtract. choose numbers to subtract')
    b = int(input())
    n = int(input())
    print(b - n)
    

    

if calculate == 'divide':
    print('you selected divide. choose numbers to divide')
    p = int(input())
    m = int(input())
    print(p / m)


if calculate == 'exponet':
    print('you selected exponet. choose numbers to exponet')
    l = int(input())
    e = int(input())
    print(l ** e)
