class item:
    def __init__(self,name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

class shoppingCart:
    def __init__(self):
        self.items=[]
        self.total_price=0

    def add_item(self,item_name, price, quantity):
        new_item=item(item_name, price, quantity)
        
        self.items.append(new_item)

        self.total_price+=new_item.price*new_item.quantity

    def remove_item(self,item_name):
        for it in self.items:
            if(it.name==item_name):
                self.total_price-=it.price*it.quantity
                self.items.remove(it)

    def calculate_total(self):
        return self.total_price
    
    def display_cart(self):
        for it in self.items:
            print(it.name,it.price,it.quantity)
        print(self.total_price)

cart1=shoppingCart()

cart1.add_item("cheese",444,2)
cart1.add_item("potato",123,3)

cart1.add_item("milk",1000,6)

cart1.display_cart()

cart1.remove_item("potato")

cart1.display_cart()