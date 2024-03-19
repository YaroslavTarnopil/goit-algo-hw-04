def total_salary(path):
    try:
       with open(path, 'r', encoding= 'utf-8') as file:
           lines = file.readlines()
       total_salary = 0 
       num_developers = len(lines)
       for line in lines:
           _, salary_str = line.split(',')
           total_salary += int(salary_str)
       average_salary = total_salary / num_developers
       return total_salary, average_salary
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None, None
jls_extract_var = r"d:\\Projects VS Code\\got-algo-hw-04\\file.txt"
total, average = total_salary(jls_extract_var)
if total is not None and average is not None:
    print(f"Загальна сума зарібної плати: {total}, Середня заробітна плата: {average}")        
          