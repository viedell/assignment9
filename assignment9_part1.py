numbers = []
print("Enter 10 numbers!: ")
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
total = sum(numbers)
print("List: ", numbers)
print("Total elements: ", total)