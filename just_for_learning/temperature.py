import datetime


class TemperatureRecordSystem:
    def __init__(self):
        self.company_name = ""
        self.company_address = ""
        self.record_days = 0
        self.temperature_dict = {}
        self.localtime = datetime.date.today().strftime("%d %B %Y")

    def initial_display(self):
        display = f'''              {self.company_name} Temperature Record Management System
                             {self.company_address} Nepal
                              {self.localtime}
    --------------------------------------------------------------------------
      '''
        print(display)

    def input_information(self):
        self.company_name = input("Company Name: ")
        self.company_address = input("Company Address: ")
        self.record_days = int(input("How many days to record? "))

        self.initial_display()

        print(f'Please enter {self.record_days} temperature readings')

        for i in range(self.record_days):
            temperature = int(input(f'Temperature day {[i + 1]} = '))
            self.temperature_dict[i] = temperature

    def category_check(self, temperature):
        if temperature > 85:
            return 'Very hot day'
        elif 60 <= temperature <= 85:
            return 'Pleasant day'
        else:
            return 'Very cold day'

    def calculate_temperature(self):
        temp = 0
        total_hot_days = 0
        total_pleasant_days = 0
        total_cold_days = 0

        for temperature in self.temperature_dict.values():
            temp += temperature

            if temperature > 85:
                total_hot_days += 1
            elif 60 <= temperature <= 85:
                total_pleasant_days += 1
            else:
                total_cold_days += 1

        avg_temp = temp / len(self.temperature_dict)

        return avg_temp, total_hot_days, total_pleasant_days, total_cold_days

    def final_display(self):
        self.input_information()
        average_temp, hot_days, pleasant_days, cold_days = self.calculate_temperature()

        self.initial_display()

        print('----------------------------------------------------')
        print('Daily Temperature Report')
        print('----------------------------------------------------')

        for day, temp in self.temperature_dict.items():
            print(f'Temperature for Day {day} = {temp} Celsius ({self.category_check(temp)})')

        print(f'The average temperature over {self.record_days} days = {average_temp:.2f} Celsius')
        print(f'Number of hot days = {hot_days} day(s)')
        print(f'Number of pleasant days = {pleasant_days} day(s)')
        print(f'Number of cold days = {cold_days} day(s)')

        print('-----------------------------------------------------')


record_system = TemperatureRecordSystem()


record_system.final_display()