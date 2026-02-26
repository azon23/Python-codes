# liste de dictionnaires
society = [
    {'Name': 'Alan Turing', 'Salary': 10000},
    {'Name': 'Sharon Lin', 'Salary': 8000},
    {'Name': 'John Hopkins', 'Salary': 1000},
    {'Name': 'Mikhail Tal', 'Salary': 15000},
    ]

# retourne la valeur de la clé "Name"
def get_name(employee):
    return employee.get('Name')

# retourne la valeur de la clé "Salary"
def get_salary(employee):
    return employee.get('Salary')

# affiche les noms et salaires
for employee in society:
    name = get_name(employee)
    salary = get_salary(employee)
    print(name, ":", salary, '€')