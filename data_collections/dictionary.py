dict1 = {'Name': 'Zara', 'Age': 12, 'Class': 'First'}
print(dict1)
print(type(dict1))
print(dict1["Name"])

dict1["Age"] = 8
dict1["School"] = "DPS School"
dict1.update({"Location": "Kochi"})
print(dict1)

del dict1["Name"]
dict1.clear()
# del dict1
print(dict1)


employees = {
    1000: {'eid': 1000, 'name': 'Jack', 'salary': 25000, 'designation': 'Developer'},
    1001: {'eid': 1001, 'name': 'Ram', 'salary': 35000, 'designation': 'Tester'}
}
# print(employees[1001]['name'])

emp_id = int(input("Enter the id: "))
if emp_id not in employees:
    print("Emp id is not present")
else:
    key = input("Enter the key: ")
    if key not in employees.get(emp_id, {}):
        print("key is not present")
    else:
        print(employees[emp_id][key])

# if emp_id not in employees and key in employees[emp_id]:
#     print(employees[emp_id][key])
# else:
#     print("Invalid id or key")
