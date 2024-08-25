def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

# for i in g:
#     print(i)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

print(sum(g))
















