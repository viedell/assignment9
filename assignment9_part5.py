shopping_list = []
print("Enter 5 shopping items:")
for i in range(5):
    item = input(f"Item {i+1}: ")
    shopping_list.append(item)

print("Your Shopping List:", shopping_list)

item_to_remove = input("Enter one item to remove (purchased): ")
if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print("Updated Shopping List:", shopping_list)
else:
    print("Item not found in the list.")