'''Екі бүтін А және В саны берілген, A>B.
   А-дан В-ға дейінгі барлық тақ сандарды кему ретімен басып шығарыңыз.
   Бұл тапсырмада if операторынсыз орындай аласыз
'''
A=int(input("A= "))
B=int(input("B= "))
for i in range(A - (A + 1) % 2, B - B % 2, -2):
    print(i, end=' ')
      