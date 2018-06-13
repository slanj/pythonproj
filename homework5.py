balance = 999999
annualInterestRate = 0.18

def remaining_balance(balance, ann, pay, n=12):
    if n == 0:
        return round(balance, 2)
    else:
        rbalance = (remaining_balance(balance, ann, pay, n-1) - pay) * (1+(ann/12))
        return round(rbalance, 2)

def find_payment(balance, ann):
    lpay = round(balance/12, 2)
    upay = round(balance*((1+(ann/12))**12), 2)
    payment = round((lpay+upay)/2, 2)

    while abs(remaining_balance(balance, ann, payment)) >= 1:
        test = remaining_balance(balance, ann, payment)
        if remaining_balance(balance, ann, payment) > 0:
            lpay = payment
        else:
            upay = payment
        payment = round((lpay+upay)/2, 2)

    print(payment)
    return payment

find_payment(balance, annualInterestRate)