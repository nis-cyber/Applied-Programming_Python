import smtplib


class Student:

    def __init__(self, name, address, phone, gender, email, grade):
        self.iukl_code = ""
        self.name = name
        self.address = address
        self.phone = phone
        self.gender = gender
        self.email = email
        self.grade = grade
        self.category = ""
        self.discount = 0
        self.admission_amount = 0
        self.discounted_amount = 0

    def get_name(self):
        return self.name

    def set_iukl_code(self, code):
        self.iukl_code = code

    def input_student_info(self):
        self.name = input("Enter student name (first last): ")
        self.address = input("Enter student address: ")
        self.phone = input("Enter student phone: ")
        self.gender = input("Enter student gender: ")
        self.email = input("Enter student email: ")
        self.grade = int(input("Enter student grade percentage: "))

        if self.grade > 80:
            self.category = "A"
            self.discount = 60
        elif self.grade > 70:
            self.category = "B"
            self.discount = 50
        elif self.grade > 60:
            self.category = "C"
            self.discount = 40
        else:
            self.category = "D"
            self.discount = 20

    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"IUKL Code: {self.iukl_code}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")
        print(f"Gender: {self.gender}")
        print(f"Email: {self.email}")
        print(f"Grade: {self.grade}")
        print(f"Category: {self.category}")
        print(f"Discount: {self.discount}%")

    def register_student(self):
        print("Registering student...")
        self.set_iukl_code("IUKL" + self.name)
        self.input_student_info()
        self.send_registration_email()
        print("Student registered successfully!")

    def send_registration_email(self):
        message = f"Dear Admin,\n\nNew student has been registered:\nName: {self.name}\nIUKL Code: {self.iukl_code}\n\nRegards,\nIUKL University"
        email = "admin@iukl.com.np"

        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login('abc@gmail.com', 'password')
            smtp.sendmail('abc@gmail.com', email, message)
            smtp.close()
            print("Registration email sent successfully!")
        except Exception as ex:
            print("Error: email failed", ex)


student1 = Student("", "", "", "", "", 0)
student1.register_student()
student1.display_student_info()