import json

inventory = [
    {"make": "Toyota", "model": "Camry", "year": 2022, "price": 25000},
    {"make": "Honda", "model": "Civic", "year": 2023, "price": 22000},
    {"make": "Tesla", "model": "Model 3", "year": 2024, "price": 42000},
    {"make": "Ford", "model": "Focus", "year": 2021, "price": 18000},
    {"make": "BMW", "model": "X5", "year": 2023, "price": 60000}
]

def search_by_budget(inventory, max_price):
    
    filtered_inventory = []
    filtered_inventory = [car for car in inventory if car["price"] <= max_price]
    return filtered_inventory


def save_inventory(inventory, filename):
    with open(filename, 'w') as file:
        json.dump(inventory, file, indent=4)
    return filename

if __name__ == "__main__":
    max_price = float(input("Enter the maximum price: "))
    filtered_inventory = search_by_budget(inventory, max_price)
    print("Cars within the budget:")
    
    if filtered_inventory:
        for car in filtered_inventory:
            print(f"Make: {car['make']}, Model: {car['model']}, Year: {car['year']}, Price: ${car['price']}")
    else:
        print("No cars found within the specified budget.")

        filename="car_inventory.json"
        saved_filename = save_inventory(inventory, filename)
        print(f"Inventory saved to {saved_filename}")

