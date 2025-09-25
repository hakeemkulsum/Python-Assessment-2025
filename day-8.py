#STACKS:
stack=[]
stack.append(6)
print(stack)

#

n=len(students)
while students and sandwiches and sandwiches[0] in students:
    if students[0]!=sandwiches[0]:
        students.append(students.pop(0))
    else:
        students.pop(0)
        sandwiches.pop(0)
        n-=1
        return n