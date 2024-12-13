# Accept a string and perform reversal of character 
# in string.except special characters
str = input("Enter the string")
#str = "H@e!ll$o"
lst = list(str)
sind = 0
lind = len(str)-1
print(str)
while sind < lind :
    if not lst[sind].isalpha():
        sind+=1
    elif not lst[lind].isalpha():
        lind-=1
    else:
        lst[sind],lst[lind] = lst[lind],lst[sind]
        sind+=1
        lind-=1
print(" ".join(lst))
