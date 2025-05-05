fruits = []
print("Enter 5 fruit name!")
for i in range(5):
    fruit = input(f"Fruit {i+1}: ")
    fruits.append(fruit)
print("Fruit list: ", fruits)
print("Fruit at index 2: ", fruits[2])
new_fruit = input("Enter new fruit: ")
fruits.append(new_fruit)
print("Updated fruit list:", fruits)