#Created by Andre Menezes
amount = float(input('Enter amount: '))
month = float(input('How many months? '))
num = 0
def calculate(amount,month,num):
    while num != month:
        interest = amount * 0.12
        total = amount + interest
        amount = total
        num += 0.25
        print('Month: ',((num*4)/4),'total = ',round(total,2))
calculate(amount,month,num)

