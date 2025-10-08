Name = input("Please enter your name: ")
GPA = float(input("Please enter your GPA: "))
credit_hours = int(input("Please enter your credit hours: "))

deans_list_eligile = GPA >= 3.5 and credit_hours >=12

print(f'Student {Name}')
print(f'Whether they made the dean’s list: {deans_list_eligile}')
print(f'gpa points needed: {(3.5 - GPA) * (GPA <= 3.5):.2f}')
print(f"credit hours needed: {(12 - credit_hours)*(credit_hours <= 12)}")
# True = 1
# False = 0
