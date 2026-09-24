def main():
    print("Recipe & Grocery Budgeter: Proof of Concept")
    
    recipe_name = input("Enter recipe name: ")
    
    try:
        item1_cost = float(input("Enter cost of primary ingredient ($): "))
        item2_cost = float(input("Enter cost of secondary ingredient ($): "))
    except ValueError:
        print("Error: You need to enter valid numerical amounts for costs.")
        return

    total_cost = item1_cost + item2_cost
    target_budget = 15.00
  
    print("\n--- Recipe Budget Summary ---")
    print(f"Recipe Name: {recipe_name}")
    print(f"Total Calculated Cost: ${total_cost:.2f}")

    if total_cost <= target_budget:
        under_amount = target_budget - total_cost
        print(f"Budget Status: Within target (${under_amount:.2f} under limit)")
    else:
        over_amount = total_cost - target_budget
        print(f"Budget Status: Over target (${over_amount:.2f} over limit)")

if __name__ == "__main__":
    main()
