print('Shopping Receipt')
print("-----------------------")
item1 = 162*1.2
item2 = 25-3
total_items = item1 + item2
print("Item 1: $", item1)  # Price per weight
print("Item 2: $",item2)  # Discounted price
print("-----------------------")
print("Subtotal: $", total_items)
print("Tax (8%): $", total_items*8/100)
print("-----------------------")
print("Thank you for shopping!")