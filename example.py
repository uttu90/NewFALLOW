# function declaration
def changeParameters(a_array):
    a_array.append('a')
a = [1, 2, 4]

changeParameters(a)

# Other place
a = a + [5]
print a