# def typed():
#     a = 11
#     b = 12.22
#     d = True
#     e = "hello world"
#     print(type(a))
#     print(type(b))
#     # print(type(c))
#     print(type(d))
#     print(type(e))


# # typed()


# def system():
#     a = 10
#     b = 0o10
#     c = 0X10
#     d = 0B10
#     print(a)
#     print(b)
#     print(c)
#     print(d)


# # system()
# for i in range(10):
#     if (i <= 6):
#         continue
#     else:
#         print(i)


# def listt():
#     list = [1, 2, 3, 4, 'ram', 7.7, -8]

#     for i in list:
#         print(i)


# listt()
# s = "learning is so joy for me"
# i = s.split()
# print(i)

# list = []
# for i in range(101):
#     if i % 5 == 0:
#         list.append(i)

# print(list)


# extend function is used to combinen two strings or arrays etc....
# order = ['pappu', 'koora', 'sambar']
# juju = ['pulusu', 'mukkalu']
# order.extend(juju)
# print(order)
# x = ['mushroom']
# order.extend(x)
# print(order)
# n = [10, 20, 30, 40]
# n.reverse()
# print(n)


# Aliasing  and cloning of list  objects :
x = [10, 20, 30, 40]
y = x[:]
print(x)
print(y)
print(id(x))
print(id(y))
y[2] = 111
print(x)
print(y)
# by using slice operator we can make possible changes
# slice operator =  :
n=[[10,20,30],[40,50,60],[70,80,90]]
print("Element Row wise : ")

# Split a string into array of characters
s = "hello world"
char_list = list(s)
print(char_list)