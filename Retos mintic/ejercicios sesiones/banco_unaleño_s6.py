bille_1 = 10000
bille_2 = 20000
bille_3 = 50000
bille_4 = 100000

retirar = int(input())

n_bill_4 = retirar//100000
retirar = retirar - (n_bill_4 * bille_4)

n_bill_3 = retirar//50000
retirar = retirar - (n_bill_3 * bille_3)

n_bill_2 = retirar//20000
retirar = retirar - (n_bill_2 * bille_2)

n_bill_1 = retirar//10000
retirar = retirar - (n_bill_1 * bille_1)

print(f"{n_bill_4} x $100000")
print(f"{n_bill_3} x $50000")
print(f"{n_bill_2} x $20000")
print(f"{n_bill_1} x $10000")