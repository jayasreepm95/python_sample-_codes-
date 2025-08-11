for n in range(1,6):
    print("* " * n)

"""rows = 5
for i in range(0, rows):
        # nested loop for each column
        for j in range(0, i + 1):
            # print star
            print(j, end=' ')
        # new line after each row

        print("\r")


"""

for i in range(1, 6):
    k = 4
    a = i
    for j in range(i, i+i):
        if(i == j):
            print(j, end=" ")
        else:
            a = a + k
            print(a, end=" ")
            k =k- 1
    print()
