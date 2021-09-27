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
        pass 
        # self.add(their_item)
        # self.remove(my_item)
        # friend.add(my_item)
        # friend.remove(their_item)
        # if my_item not in self.inventory or their_item not in friend.inventory:
        #     return False 
        # return True 
        