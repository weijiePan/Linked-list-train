class cart:

    def __init__(self, color, next_cart = None):
                self.color = color
                if(next_cart != None):
                    self.next_cart = next_cart 
                else:
                    self.next_cart = None
    
    def __repr__(self):
           
           return f" ------\n|{self.color}|\n ------ "
   

