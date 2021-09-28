class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add
    
    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False 
    
    def get_by_category(self, category):
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)
        return items_by_category 

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or \
            their_item not in friend.inventory:
            return False 

        self.remove(my_item)
        friend.add(my_item)
        friend.remove(their_item)
        self.add(their_item)
        return True 

    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False 

        self.swap_items(friend, self.inventory[0], friend.inventory[0])
        return True 

    def get_best_by_category(self, category):
        best_item, rating = "", -1
        for item in self.inventory:
            if item.category == category:
                if item.condition > rating:
                    best_item, rating = item, item.condition

        if best_item == "":
            return None 
        else:
            return best_item 
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = other.get_best_by_category(my_priority)
        their_best_item = self.get_best_by_category(their_priority)

        if my_best_item == None or their_best_item == None:
            return False 
            
        self.swap_items(other, their_best_item, my_best_item)
        return True 
# -----------------------------------------------------------------------------

class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "Yikes!"
        elif self.condition == 1:
            return "Why would you want this?"
        elif self.condition == 2:
            return "Ugh"
        elif self.condition == 3:
            return "Passable"
        elif self.condition == 4:
            return "Not bad"
        elif self.condition == 5:
            return "Great find!"
        

class Clothing(Item):
    def __init__(self, condition=0):
        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."

class Decor(Item):
    def __init__(self, condition=0):
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."

# item_a = Decor(condition=2.0)
# item_b = Electronics(condition=4.0)
# item_c = Decor(condition=4.0)
# tai = Vendor(inventory=[item_a, item_b, item_c])
    
# item_d = Clothing(condition=2.0)
# item_e = Decor(condition=4.0)
# item_f = Clothing(condition=4.0)
# jesse = Vendor(inventory=[item_d, item_e, item_f])
    
# result = tai.swap_best_by_category(other=jesse, my_priority="Clothing", their_priority="Decor")
# >       assert result
# E       assert False