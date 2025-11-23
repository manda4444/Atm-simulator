
def main():
    balance = 1000.0

    print(f"your current balance is {balance}")

    out = float(input("how much do you want to take out today ?"))

    if out > balance:
        print(f"{out} is insufficient, you have only {balance}")
    elif out == balance:
        print(f"you will have zero birr if you takeout {out} ")
        current_balance = balance - out
        print(f"you have withdrawn {out}")
        print(f"your current balance is {current_balance}")


    elif out < 0:
        print(f" Withdraw must be greater than zero ")
    else:

        print("withdrawal successful !! ")
        current_balance = balance - out
        print(f"you have withdrawn {out}")
        print(f"your current balance is {current_balance}")


main()
