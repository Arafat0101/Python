course = "Python's Course for Beginners"
print(course[0])
print(course[0:5])

another = course[-2]
print(another)

another1 = course[1:-1]
print(another1)

print(len(course))
print(course.upper())
print(course.lower())
print(course.find('t'))
print(course.replace("Python's","Java"))
print('for' in course)
print(course.title)

first = 'John'; last = 'Smith'
message = first + ' {' +last + '} is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)
