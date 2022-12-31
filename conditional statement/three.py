#Wap to print min value
x = int(input("enter the vlaue:"))
y = int(input("enter the value:"))
z = int(input("enter the value:"))
'''
if x<y and x<z:
    min = x
elif  y<z:
        min = y
else:
        min = z
'''
min = x if x<y and x<z else y if y<z else z
print(min)