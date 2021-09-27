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
        
