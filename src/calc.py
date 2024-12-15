#Calculate the total amount from the file

if __name__ == "__main__" :
    with open("cheeti.txt", "r") as fp:
        lines = fp.readlines()
    total = 0
    for l in lines:
       for n in l.split():
        if n.isdigit() :
            num = int(n)
            total += num

    print("Total Amount is ", total)