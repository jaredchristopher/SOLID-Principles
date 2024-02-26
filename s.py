# Created by: Jared Christopher
# File: s.py

# I created an order class because I wanted to be able to define what an
# order should have. An order should have customer details. It must be validated. It must have a cost, and
# a confirmation email must be sent to the customer after they pay for their order. Afterwards, it should update the inventory.
class Order:
    def __init__(self, order_details, order_validator, order_cost, order_confirm, inventory_updater):
        self.order_details = order_details
        self.order_validator = order_validator
        self.order_cost = order_cost
        self.order_confirm = order_confirm
        self.inventory_updater = inventory_updater

    # Whenever someone places an order it must be validated, calculate its cost,
    # send a confirmation email, and update the inventory
    def place_order(self):
        if self.order_validator.validate():
            total_cost = self.order_cost.calculate_total_cost()
            self.order_confirm.send_confirmation()
            self.inventory_updater.update_inventory()
            return total_cost
        else:
            return "Order validation failed. Please check your order details."

# OrderDetails has the parameters cutomer_name, items, and shipping_address
# which is what I deemed as the necessary information for the order.
class OrderDetails:
    def __init__(self, customer_name, items, shipping_address):
        self.customer_name = customer_name
        self.items = items
        self.shipping_address = shipping_address

# OverValidator should check the order details and make sure that they are all satisfied (!None)
class OrderValidator:
    def __init__(self, order_details):
        self.order_details = order_details

    def validate(self):
        if self.order_details:
            return True
        else:
            return False

# Calcualtes the cost of the order based on how many items are being purchased
# In John Doe's, case there will be 3 items.
class OrderCost:
    def __init__(self, order_details):
        self.order_details = order_details

    def calculate_total_cost(self):
        if self.order_details:
            purchase_total = len(self.order_details.items) * 10
            return f"${purchase_total}"
        else:
            return 0
        
# Sends the confirmation email to the customer once 
# their purchase has been validated and paid for
class OrderConfirm():
    def __init__(self, email, order_validator):
        self.email = email
        self.order_validator = order_validator

    def send_confirmation(self):
        if self.order_validator.validate():
            return f"An order confirmation email has been sent to you at: {self.email}"
        else:
            return "We could not validate your purchase."

# Subtracts the numof_items from the total_inventory
class UpdateInventory:
    def __init__(self, numof_items):
        self.numof_items = numof_items

    def update_inventory(self):
        total_inventory = 100
        new_total_inventory = total_inventory - self.numof_items
        return f"Amount left in inventory: {new_total_inventory}"

def main():
    customer_name = "John Doe"
    items = ["Pants", "Socks", "T-Shirts"]
    shipping_address = "123 Main St, Citytown"
    email = "john.doe@gmail.com"
    num_of_items = len(items)

    order_details = OrderDetails(customer_name, items, shipping_address)
    print("Order details:", order_details.customer_name, order_details.items, order_details.shipping_address)

    order_validator = OrderValidator(order_details)
    print("Order validation result:", order_validator.validate())

    order_cost = OrderCost(order_details)

    order_confirm = OrderConfirm(email, order_validator)
    print("Confirmation email:", order_confirm.send_confirmation())

    inventory_updater = UpdateInventory(num_of_items)
    print(inventory_updater.update_inventory())

    order = Order(order_details, order_validator, order_cost, order_confirm, inventory_updater)
    
    total_cost = order.place_order()
    print("Total order cost:", total_cost)

if __name__ == "__main__":
    main()
    