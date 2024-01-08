def calculate_bill(units_consumed):
    if units_consumed < 80:
        per_unit_price = 4
        discount = 0
        service_charge = 0
    elif units_consumed < 150:
        per_unit_price = 10
        discount = 5
        service_charge = 5
    elif units_consumed < 250:
        per_unit_price = 12
        discount = 8
        service_charge = 5
    elif units_consumed < 350:
        per_unit_price = 15
        discount = 10
        service_charge = 8
    elif units_consumed < 500:
        per_unit_price = 18
        discount = 12
        service_charge = 10
    else:
        per_unit_price = 20
        discount = 15
        service_charge = 12

    total_bill_amount = units_consumed * per_unit_price
    total_amount = total_bill_amount + service_charge
    price_after_discount = total_amount - discount

    return total_bill_amount, service_charge, discount, price_after_discount


def main():
    print("****************Unicampus Electricity Company***************")
    print("Putalisadak, Kathmandu")
    print("------------------------------------------------------------------------")

    customer_name = input("Please enter Name of the Customer: ")
    customer_address = input("Please enter Address of the Customer: ")
    customer_phone = input("Please enter Phone No of the Customer: ")
    units_consumed = float(input("Please enter Number of Unit you consumed: "))

    total_bill, service_charge, discount, price_after_discount = calculate_bill(units_consumed)

    print("\nOutput:")
    print("****************Unicampus Electricity Company***************")
    print("Putalisadak, Kathmandu")
    print("------------------------------------------------------------------------")
    print(f"Customer Name: {customer_name} Address: {customer_address}")
    print(f"Phone: {customer_phone} Total Unit Consumed: {units_consumed}")
    print(f"Bill Amount: {total_bill} Service Charge: {service_charge}")
    print(f"Total Amount: {total_bill} + {service_charge} = {total_bill + service_charge}")
    print(f"Total Discount: {discount}")
    print(f"Price After Discount: {price_after_discount}")
    print(f"Your total bill is: {total_bill + service_charge} and Mr. {customer_name}, you got a discount of {discount}, so the discounted price is {price_after_discount}.")


if __name__ == "__main__":
    main()
