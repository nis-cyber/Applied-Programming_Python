
def convert(weight_pounds,height_inches):
    weight_kg = weight_pounds * 0.45359237
    height_m = height_inches * 0.0254

    return weight_kg,height_m


def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / height_m**2
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        interpretation = "Underweight"
    elif bmi < 25:
        interpretation = "Normal"
    elif bmi < 30:
        interpretation = "Overweight"
    else:
        interpretation = "Obese"
    return interpretation

def main():
    # Prompt user to enter weight in pounds and height in inches
    weight_pounds = float(input("Enter weight in pounds: "))
    height_inches = float(input("Enter height in inches: "))

    # Convert weight from pounds to kilograms
    weight_kg = convert(weight_pounds)

    # Convert height from inches to meters
    height_m = convert(height_inches)

    # Calculate BMI
    bmi = calculate_bmi(weight_kg, height_m)

    # Interpret BMI
    interpretation = interpret_bmi(bmi)

    # Display BMI and interpretation
    print("BMI:", bmi)
    print("Interpretation:", interpretation)

if __name__ == "__main__":
    main()
