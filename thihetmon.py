import math
def isPrimeNumber(n):
    if (n < 2):
        return False
    nt = int(math.sqrt(n))
    for i in range(2, nt + 1):
        if (n % i == 0):
            return False
    return True
n = int(input("Nhập số nguyên tố n = "))
print ("Tất cả các số nguyên tố nhỏ hơn", n, "là:")
ab = ""
if (n >= 2):
    ab = ab + "2" +  " "
for i in range (3, n+1):
    if (isPrimeNumber(i)):
        ab = ab + str(i) + " "
    i = i + 2
print(ab)