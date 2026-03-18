# Listas ^^ Tuplas


list_mix = [1, 2, 3, 'Hola', True, 3.14]

# print(list_mix)

# real life example
students = ['Alice', 'Bob', 'Charlie']
grades = [85, 92, 78]



# List slicing - rebanar [inicio : fin]

shopping_cart = ['apple', 'banana', 'orange', 'grape', 'kiwi']

new_cart = shopping_cart[0:4]  # ['banana', 'orange', 'grape']

# print(shopping_cart[0:2])
# print(shopping_cart)



# print(new_cart)

# mutar la listaq
new_cart[0] = 'pear'
# print(new_cart) #pear

# *ejercicio copiar una lista
new_list =  ["pedro", "maria", "juan"]

# copiando una lista completa - no es recomendable usar el operador de asignación (=) porque ambas variables apuntarán a la misma lista en memoria, lo que puede causar problemas si se modifica una de las listas.
copied_list = new_list[:]  # Copia de la lista

# print(new_list)     # ['pedro', 'maria', 'juan']
# print(copied_list)  # ['pedro', 'maria', 'juan']
copied_list.append("Ana")
# print(copied_list)  # ['pedro', 'maria', 'juan', 'Ana']



# metodos de agregacion

# append() - agrega un elemento al final de la lista
shopping_cart.append('melon')
# print(shopping_cart) # ['apple', 'banana', 'orange', 'grape
# insert() - agrega un elemento en una posición específica
shopping_cart.insert(2, 'pear')

# extend() - agrega los elementos de otra lista al final de la lista actual
new_items = ['watermelon', 'peach']
shopping_cart.extend(new_items)






my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
print(my_str[-1]) # d


first_name = 'John'
last_name = 'Doe'
print(f"{first_name}{last_name}") # Output: Hello


employee_age = 28
print(type (employee_age))

print(type(str(employee_age)))



# first_name = 'John'
# last_name = 'Doe'
# full_name = first_name + ' ' + last_name
# address = '123 Main Street'
# address += ', Apartment 4B'
# employee_age = 28
# employee_info = full_name + ' is ' + str(employee_age) + ' years old'
# print(employee_info)
# experience_years = 5
# experience_info = 'Experience: ' + str(experience_years) + ' years'
# print(experience_info)
# position = 'Data Analyst'
# salary = 75000
# employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
# print(employee_card)
# employee_code = 'DEV-2026-JD-001'
# department = employee_code[0:3]
# print(department)
# year_code = employee_code[4:8]
# print(year_code)
# initials = employee_code[9:11]
# print(initials)

# # Add this line:
# last_three = employee_code[-3:]  # Gets the last 3 characters
# print(last_three)
