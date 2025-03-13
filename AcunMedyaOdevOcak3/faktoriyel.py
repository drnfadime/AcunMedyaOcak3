sayi = int(input("Faktöriyeli hesaplanacak sayıyı giriniz:"))
faktoriyel = 1
for i in range(1,sayi+1):
    faktoriyel *= i

print(f"{sayi}! = {faktoriyel}")
