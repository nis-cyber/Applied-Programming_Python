def calculate_income_tax(income):
    if income <= 400000:
        tax = income * 0.01
    elif income <= 500000:
        tax = 4000 + (income - 400000) * 0.1
    elif income <= 700000:
        tax = 14000 + (income - 500000) * 0.2
    elif income <= 2000000:
        tax = 54000 + (income - 700000) * 0.3
    else:
        tax = 624000 + (income - 2000000) * 0.36

    return tax


def main():
    income = float(input("Enter the income level (NPR): "))
    tax = calculate_income_tax(income)
    print(f"The income tax for NPR {income} is NPR {tax:.2f}")


if __name__ == "__main__":
    main()
