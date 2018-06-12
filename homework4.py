balance = 88
annualInterestRate = 0.2
monthlyPaymentRate = 0.06

def remaining_balance(balance, ann, mon, n=12):
    if n == 0:
        rbalance = balance
        return round(rbalance, 2)
    else:
        rbalance = remaining_balance(balance, ann, mon, n-1)
        p = rbalance * mon
        rbalance = (rbalance - p) * (1+(ann/12))
        return round(rbalance, 2)



print(remaining_balance(balance, annualInterestRate, monthlyPaymentRate))