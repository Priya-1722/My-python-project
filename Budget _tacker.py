print("🛒 WELCOME TO YOUR MOBILE BUDGET TRACKER 🛒")

# Ask the user for their total spending limit
budget = float(input("Enter your total budget amount: "))
total_spent = 0

while True:
    print(f"\nRemaining Budget: ${budget - total_spent:.2f}")
    
    item = input("Enter item name (or type 'done' to finish): ")
    if item.lower() == 'done':
        print("\nClosing your tracker...")
        break
        
    price = float(input(f"Enter price for {item}: "))
    
    # Add the price to our running total
    total_spent = total_spent + price
    
    # Check if we went over budget
    if total_spent > budget:
        print(f"⚠️ WARNING! You have exceeded your budget by ${total_spent - budget:.2f}!")
    else:
        print(f"✅ Added {item}. Total spent so far: ${total_spent:.2f}")

print(f"\nFinal Summary: You spent a total of ${total_spent:.2f} out of ${budget:.2f}.")
