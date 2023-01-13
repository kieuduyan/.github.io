start = 2
end = 11
for i in range(start,end):
    start = 1
    for j in range(1, 11):
        print("(:<3 X {:<3} = {:<3}".format(start, j, start*j))
    print("")
