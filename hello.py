print('Hello World')
number = 31
name = "What"

print(number, name)

if number == 21:
    print("Number is 21")
else:
    print("Number is not 21")

if name:
    print("This is real")

if number == 21 and name:
    print("answer and name pass")

if number != 21 or name:
    print("answer and name pass")

a = 1
b = 2

ternaryOperationValue = "bigger" if a > b else "smaller"

print(ternaryOperationValue);

student_names = ["Mark", "Tiff", "Ted"]
print(student_names[0])
print(student_names[-1])  # Gets last item

print(len(student_names))  # Gets length of list
del student_names[2]  # Deletes that item in list

print(student_names[1:])  # Does not delete just modifies what is shown


