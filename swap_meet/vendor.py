from operator import attrgetter

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
    
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
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or \
            their_item not in other.inventory:
            return False 
        else: 
            other.add(self.remove(my_item))
            self.add(other.remove(their_item))
            return True 

    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False 
        else:
            my_first, their_first = self.inventory[0], friend.inventory[0]
            return self.swap_items(friend, my_first, their_first)

    def get_best_by_category(self, category): 
        if len(self.get_by_category(category)) == 0:
            return None 
        else: 
            items_of_this_category = self.get_by_category(category)
            return max(items_of_this_category, key=attrgetter("condition"))
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_best_item, their_best_item)

    def get_newest_item(self):
        if len(self.inventory) == 0:
            return None 
        else:
            return min(self.inventory, key=attrgetter("age"))

    def swap_by_newest(self, other):
        my_newest_item = self.get_newest_item()
        their_newest_item = other.get_newest_item()
        return self.swap_items(other, my_newest_item, their_newest_item)