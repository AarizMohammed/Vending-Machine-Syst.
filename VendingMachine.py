class Shelf:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def dispense_product(self):
        if self.quantity > 0:
            self.quantity -= 1
            return self.name
        else:
            return None

    def __str__(self):
        return f"{self.name}. {self.quantity} left, ${self.price:.2f}"

class VendingMachine:
    def __init__(self, shelves):
        self.shelves = shelves
        self.credit = 0.0

    def insert_money(self, amount):
        self.credit += amount

    def get_machine_state(self):
        return "\n".join(str(shelf) for shelf in self.shelves) + f"\n${self.credit:.2f} credit"

    def vend_item(self, shelf_index):
        if 0 <= shelf_index < len(self.shelves):
            selected_shelf = self.shelves[shelf_index]
            if selected_shelf.price <= self.credit and selected_shelf.quantity > 0:
                product_name = selected_shelf.dispense_product()
                self.credit -= selected_shelf.price
                return f"Vend successful! Enjoy your {product_name}."
            elif selected_shelf.quantity == 0:
                return "Vend failed. Out of stock."
            else:
                return "Vend failed. Insufficient credit."
        else:
            return "Invalid shelf index."

    def return_change(self):
        change = self.credit
        self.credit = 0.0
        return f"Change returned: ${change:.2f}"

    def __str__(self):
        return "\n".join(str(shelf) for shelf in self.shelves) + f"\n${self.credit:.2f} credit"




class BreakRoom:
    def __init__(self, vm1, vm2):
        self.vending_machines = [vm1, vm2]

    def simulate(self):
        while True:
            print("Welcome to the Break Room!")
            for i, machine in enumerate(self.vending_machines, start=1):
                print(f"{i}. {machine}")
            print("What would you like to do?")
            print("1. Enter money")
            print("2. Get change back")
            print("3. Vend an item")
            print("4. Leave the break room")

            choice = input("Your Choice? ")
            
            if choice == "1":
                amount = float(input("Enter the amount: "))
                vm_choice = int(input("Choose a vending machine (1 or 2): ")) - 1
                self.vending_machines[vm_choice].insert_money(amount)

            elif choice == "2":
                vm_choice = int(input("Choose a vending machine (1 or 2): ")) - 1
                print(self.vending_machines[vm_choice].return_change())

            elif choice == "3":
                vm_choice = int(input("Choose a vending machine (1 or 2): ")) - 1
                shelf_choice = int(input("Which item?\n1. USB sticks\n2. iPad minis\n3. Sony Walkmans\nYour choice? ")) - 1
                print(self.vending_machines[vm_choice].vend_item(shelf_choice))

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose again.")





# Sample data for testing
shelf1 = Shelf("Chocolate bars", 8, 1.00)
shelf2 = Shelf("Sodas", 3, 1.50)

vm1 = VendingMachine([shelf1, shelf2])

shelf3 = Shelf("USB sticks", 3, 10.00)
shelf4 = Shelf("iPad minis", 1, 369.99)
shelf5 = Shelf("Sony Walkmans", 10, 79.99)

vm2 = VendingMachine([shelf3, shelf4, shelf5])

break_room = BreakRoom(vm1, vm2)
break_room.simulate()


