value = str(input("Enter a string: "))
for i in range(0,len(value)):
    if (value[i] == "a" or value[i] == "A"):
        break
    else:
        print(value[i])