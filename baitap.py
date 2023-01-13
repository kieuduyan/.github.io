def hoten (a):
    return lambda thongtin:a + ": " + thongtin
print("hãy nhập vào họ và tên ")  
a = input()
#khởi tạo account 
account = hoten(a)
print("hãy nhập vào ngày tháng năm sinh")
print(account(input()))
print("hãy nhập giới tính")
print(account(input()))
print("hãy nhập địa chỉ thường trú")
input(account(input()))