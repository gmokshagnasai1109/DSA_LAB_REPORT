def search_employee(ids, target, index):
    if index == len(ids):
        return False

    if ids[index] == target:
        return True

    return search_employee(ids, target, index + 1)


ids = [101, 102, 103, 104, 105]

target = int(input("Enter employee ID to search: "))

if search_employee(ids, target, 0):
    print("Employee ID found")
else:
    print("Employee ID not found")
    
