balance = 3926
annualInterestRate = 0.2

def remaining_balance(balance, ann, pay, n=12):
    if n == 0:
        return round(balance, 2)
    else:
        rbalance = (remaining_balance(balance, ann, pay, n-1) - pay) * (1+(ann/12))
        return round(rbalance, 2)

def find_payment(balance, annualInterestRate):
    payment = 10

    while remaining_balance(balance, annualInterestRate, payment) >= 0:
        payment += 10
    print(payment)
    return payment

find_payment(balance, annualInterestRate)