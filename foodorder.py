class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self):
        self.food_items = []
        self.food_id_counter = 1

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = self.food_id_counter
        self.food_id_counter += 1
        food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("New food item added with ID:", food_id)
    
    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item with ID", food_id, "edited successfully.")
                return
        print("Food item with ID", food_id, "This is not corect food id")
    
    def view_food_items(self):
        for food_item in self.food_items:
            print("ID:", food_item.food_id)
            print("Name:", food_item.name)
            print("Quantity:", food_item.quantity)
            print("Price:", food_item.price)
            print("Discount:", food_item.discount)
            print("Stock:", food_item.stock)
            
    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item with ID", food_id, "removed successfully.")
                return
        print("Food item with ID", food_id, "not found.")

class User:
    def __init__(self, name, phone_number, email, address, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []
        self.orders=[]
    
    def place_new_order(self, food_ids):
        ordered_items = []
        for food_item in admin.food_items:
            if food_item.food_id in food_ids:
                ordered_items.append(food_item)
        self.orders.append(ordered_items)
        print("Order placed successfully!")

    def view_order_history(self):
        for order in self.order_history:
            print("Order ID:", order.order_id)
            
    def update_profile(self, name, phone_number, email, address, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        print("Profile updated successfully.")

admin = Admin()
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 500)
admin.add_food_item("Vegan Burger", "1 piece", 120, 0, 100)
admin.add_food_item("Truffle Cake", "500g", 750, 0, 200)
admin.view_food_items()
admin.edit_food_item(2, "Vegan Burger", "2 pieces", 400, 0, 800)
admin.view_food_items()
admin.remove_food_item(3)
admin.view_food_items()

user = User("Ganesh", "1234567890", "ganesh@gmail.com", "000hyd, City", "password")
user.place_new_order([2,3])
user.view_order_history()
user.update_profile("Ganesh", "1236778765", "ganesh@.com", "111hyd, City", "newpassword")








