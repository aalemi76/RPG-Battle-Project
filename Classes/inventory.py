

#Item Class
class Item:
    #init function to initialize Item Class
    def __init__(self, name, type, description, prop, quantity):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop
        self.quantity = quantity

    #Reduce Quantity of Item whenever player utilizes it
    def reduce_quantity(self):
        self.quantity -= 1
        if self.quantity < 0:
            self.quantity = 0
        return self.quantity