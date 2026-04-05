# # # Listas ^^ Tuplas


# # list_mix = [1, 2, 3, 'Hola', True, 3.14]

# # # print(list_mix)

# # # real life example
# # students = ['Alice', 'Bob', 'Charlie']
# # grades = [85, 92, 78]



# # # List slicing - rebanar [inicio : fin]

# # shopping_cart = ['apple', 'banana', 'orange', 'grape', 'kiwi']

# # new_cart = shopping_cart[0:4]  # ['banana', 'orange', 'grape']

# # # print(shopping_cart[0:2])
# # # print(shopping_cart)



# # # print(new_cart)

# # # mutar la listaq
# # new_cart[0] = 'pear'
# # # print(new_cart) #pear

# # # *ejercicio copiar una lista
# # new_list =  ["pedro", "maria", "juan"]

# # # copiando una lista completa - no es recomendable usar el operador de asignación (=) porque ambas variables apuntarán a la misma lista en memoria, lo que puede causar problemas si se modifica una de las listas.
# # copied_list = new_list[:]  # Copia de la lista

# # # print(new_list)     # ['pedro', 'maria', 'juan']
# # # print(copied_list)  # ['pedro', 'maria', 'juan']
# # copied_list.append("Ana")
# # # print(copied_list)  # ['pedro', 'maria', 'juan', 'Ana']



# # # metodos de agregacion

# # # append() - agrega un elemento al final de la lista
# # shopping_cart.append('melon')
# # # print(shopping_cart) # ['apple', 'banana', 'orange', 'grape
# # # insert() - agrega un elemento en una posición específica
# # shopping_cart.insert(2, 'pear')

# # # extend() - agrega los elementos de otra lista al final de la lista actual
# # new_items = ['watermelon', 'peach']
# # shopping_cart.extend(new_items)






# # my_str = "Hello world"

# # print(my_str[0])  # H
# # print(my_str[6])  # w
# # print(my_str[-1]) # d


# # first_name = 'John'
# # last_name = 'Doe'
# # print(f"{first_name}{last_name}") # Output: Hello


# # employee_age = 28
# # print(type (employee_age))

# # print(type(str(employee_age)))



# # # first_name = 'John'
# # # last_name = 'Doe'
# # # full_name = first_name + ' ' + last_name
# # # address = '123 Main Street'
# # # address += ', Apartment 4B'
# # # employee_age = 28
# # # employee_info = full_name + ' is ' + str(employee_age) + ' years old'
# # # print(employee_info)
# # # experience_years = 5
# # # experience_info = 'Experience: ' + str(experience_years) + ' years'
# # # print(experience_info)
# # # position = 'Data Analyst'
# # # salary = 75000
# # # employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
# # # print(employee_card)
# # # employee_code = 'DEV-2026-JD-001'
# # # department = employee_code[0:3]
# # # print(department)
# # # year_code = employee_code[4:8]
# # # print(year_code)
# # # initials = employee_code[9:11]
# # # print(initials)

# # # # Add this line:
# # # last_three = employee_code[-3:]  # Gets the last 3 characters
# # # print(last_three)


# # distance_mi = 0
# # is_raining = False
# # has_bike = False
# # has_car = False
# # has_ride_share_app = False

# # if not distance_mi:
# #     print(False)

# # elif distance_mi <= 1 and not is_raining:
# #     print(True)

# # elif distance_mi <= 6 and has_bike and not is_raining:
# #     print(True)

# # elif distance_mi > 6 and (has_car or has_ride_share_app):
# #     print(True)

# # else:
# #     print(False)

# # def apply_discount(price, discount):
# #     if type(price) != 'number' or type(price) != 'float':
# #         return 'The price should be a number'
    
# #     if type(discount) != 'number' or type(discount) != 'float':
# #         return 'The discount should be a number'
    
# #     if price <= 0:
# #         return 'The price should be greater than 0'
    
# #     if discount < 0 or discount > 100:
# #         return 'The discount should be between 0 and 100.'
# #     return


# def caesar(text, shift, encrypt=True):

#     if not isinstance(shift, int):
#         return 'Shift must be an integer value.'

#     if shift < 1 or shift > 25:
#         return 'Shift must be an integer between 1 and 25.'

#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     if not encrypt:
#         shift = - shift
    
#     shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#     translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
#     encrypted_text = text.translate(translation_table)
#     return encrypted_text

# def encrypt(text, shift):
#     return caesar(text, shift)
    
# def decrypt(text, shift):
#     return caesar(text, shift, encrypt=False)

# encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
# decrypted_text  = decrypt(encrypted_text, 13)
# print(encrypted_text)
# print(decrypted_text)


# # ! Construir un Personaje de RPG

# full_dot = '●'
# empty_dot = '○'

# def create_character(name, strength, intelligence, charisma):
#     if not isinstance(name, str):
#         return 'The character name should be a string'
    
#     if name == '':
#         return 'The character should have a name'

#     if len(name) > 10:
#         return 'The character name is too long'

#     if ' ' in name:
#         return 'The character name should not contain spaces'
    

#     if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
#         return 'All stats should be integers'
    
#     if strength < 1 or intelligence < 1 or charisma < 1:
#         return 'All stats should be no less than 1'
    
#     if strength > 4 or intelligence > 4 or charisma > 4:
#         return 'All stats should be no more than 4'
    
#     if strength + intelligence + charisma != 7:
#         return 'The character should start with 7 points'
    

#     strength_bar = full_dot * strength + empty_dot * (10 - strength)
#     intelligence_bar = full_dot * intelligence + empty_dot * (10 - intelligence)
#     charisma_bar = full_dot * charisma + empty_dot * (10 - charisma)
    
#     return f"{name}\nSTR {strength_bar}\nINT {intelligence_bar}\nCHA {charisma_bar}"


# print(1.5+5)


# def greet():
#     pass
    
# print(greet()) # ?

# cities = ['Los Angeles', 'London', 'Tokyo']
# cities[0]

# print(cities[0])

developer = ('Alice', 34, 'Rust Developer')

# developer[0] = 'Mario'
# print('alice'.lower() in developer)

# developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
# ids = [1, 2, 3, 4]

# for name, id in zip(developers, ids):
#     print(f'Name: {name}')
#     print(f'ID: {id}')


# even_numbers = []

# for num in range(21):
#     if num % 2 == 0:
#         even_numbers.append(num)

# print(even_numbers)




# numbers = [1, 2, 3, 4, 5]
# result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
# print(result)

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']