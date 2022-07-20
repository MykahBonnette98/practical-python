#Loan Calculator

#$50,000
money_owed = float(input('How much money do you owe, in dollars?\n'))

#3%
apr = float(input('What is the annual percentage rate?\n')) 

#$1,000
payment = float(input('What will your monthly payment be, in dollars?\n'))

#24 months
months = int(input('How many months do you want to see results?\n'))

#Divide apr by 100 to make percent, divide by 12 to make monthly
monthly_rate = apr/100/12

#added loop
for i in range(months): 

    #Add in interest
    interest_paid = money_owed * monthly_rate
    monthly_owed = money_owed + interest_paid
    if (money_owed - payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months')
        break

    #Make payment
    money_owed = money_owed - payment

    #Print
    print('Paid', payment, 'of which', interest_paid, 'was interest', end=' ')
    print('Now I owe', money_owed)

#console results before added loop
#Paid 1000.0 of which 125.0 was interest Now I owe 49000.0

#console results after added loop
# The last payment is 0.0
# You paid off the loan in 51 months