# # Body mass index (BMI) is a measure of health based on weight. It can be calculated by taking your weight in
# kilograms and dividing it by the square of your height in meters. # The interpretation of BMI for people 16 years
# and older is as follows: # BMI Interpretation # Below 18.5 Underweight # 18.5–24.9 Normal # 25.0–29.9 Overweight #
# Above 30.0 Obese # Write a program that prompts the user to enter a weight in pounds and height in inches # and
# thenj displays the BMI. # Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters.
#
# pound = int(input("Enter the weight in pounds: "))
# inches = int(input("Enter y0ur height in inches: "))
#
# weight_in_kg = pound * 0.45359237
# height_in_meter = inches * 0.0254
#
# bmi = weight_in_kg/(height_in_meter**2)
# interpretation = 0;
#
#
# if bmi<18.5:
#         interpretation = 'UnderWeight'
#         if 18.5<bmi<24.9:
#             interpretation = 'Normal'
#             if 25.0<=bmi<29.9:
#                 interpretation = 'Overweight'
#             else:
#                 interpretation = 'Obese'
#
#
#
# def initialDisplay(interpretation):
#     title = '''\t\tBMI\t\t\t\t\tInterpretation'''
#     values = f'''{bmi}\t\t\t\t{interpretation}'''
#     print(title,'\n',values)
#
#
# initialDisplay(interpretation)


weight_pound=float(input("Enter the weight in pound: "))
height_inch = float(input('Enter the height in inches: '))

weight_kg = weight_pound*0.45359237
height_meter = height_inch*0.0254

bmi = weight_kg/height_meter**2
def calc(bmi) :
    if bmi<18.5:
        interpretation = 'underweight'
    elif bmi <25:
        interpretation = 'Normal'
    elif bmi <30:
        interpretation = 'Overweight'
    else:
        interpretation = 'Obese'
    return interpretation

def main(bmi,interpretation):
    print(f'''\tBMI\t\t\t\t\tInterpretation''')
    print(f'''{bmi}\t\t\t{interpretation}''')
interpretation = calc(bmi)
main(bmi,interpretation)
































