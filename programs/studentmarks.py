mark1 = int(input("Enter marks of English: "))
mark2 = int(input("Enter marks of Chemistry: "))
mark3 = int(input("Enter marks of Biology: "))
mark4 = int(input("Enter marks of Physics: "))
mark5 = int(input("Enter marks of Maths: "))
tot_marks = mark1 + mark2 + mark3 + mark4 + mark5
print("Total Marks :", tot_marks, "\nAverage Marks :", tot_marks / 5)
if tot_marks in range(270, 301):
    print("Grade A")
elif tot_marks in range(240, 270):
    print("Grade B")
elif tot_marks in range(210, 240):
    print("Grade C")
elif tot_marks in range(180, 210):
    print("Grade D")
elif tot_marks in range(150, 180):
    print("Grade E")
else:
    print("Failed")
