## Take  input and reverse the sting in its place

str = input("Enter the string")
l = str.split(" ")
print(l)
for j in l:
    s = j[::-1]
    print(s, end=" ")
print("Printed the {0} in the reverse as {1}".format(str,s))
rev = ' '
for k in l:
    rev = k + " " + rev
print(rev, end=" ")
