def createEven(n):
    number = ''
    evens = ''
    for i in n:
        if int(i) % 2 == 0:
            evens += i
    #print(evens)
    tmp = evens[-1]
    #print(tmp)
    n.remove(tmp)
    #print(n)
    number = ''.join(n)
    number += tmp
    print(number)

s = input()
numbers = ''
for i in s:
    if i.isdigit():
        numbers+=i
ns = list(set(numbers))
ns.sort(reverse=True)
createEven(ns)


