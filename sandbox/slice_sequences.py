a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two:  ', a[3:5])
print('All but ends:', a[1:7])


x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

x = b'mongoose'
y = x[::-1]
print(y)

x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(x[::2])   # ['a', 'c', 'e', 'g']
print(x[::-2]) # ['h', 'f', 'd', 'b']
print(x[2::2])     # ['c', 'e', 'g']
print(x[-2::-2])   # ['g', 'e', 'c', 'a']
print(x[-2:2:-2])  # ['g', 'e']
print(x[2:2:-2])   # []
