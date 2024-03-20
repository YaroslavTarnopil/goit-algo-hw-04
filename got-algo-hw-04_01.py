def total_salary(path):
    total_salary = 0
    num_developers = 0

    with open(path, 'r') as file:
        for line in file:
            surname, salary_str = line.strip().split(',')
            total_salary += int(salary_str)
            num_developers += 1

   
    if num_developers > 0:
        average_salary = total_salary / num_developers
    else:
        average_salary = 0

    return total_salary, average_salary


total, average = total_salary('d:\\Projects VS Code\\got-algo-hw-04\\file.txt')
print("Total salary:", total)
print("Average salary:", average)