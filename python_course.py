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



# leetcode excercise Two sum


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]  
            


print(twoSum([2, 7, 11, 15], 9)) 



