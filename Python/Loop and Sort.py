start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for count in range(0,len(start_list)):
    aux = start_list[count]**2
    square_list.append(aux)

square_list.sort()

print square_list