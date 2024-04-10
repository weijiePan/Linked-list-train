class train:
        def __init__(self, head):
            self.head = head

        def display_train(self):
            currentCart = self.head
            print(" ___ |[]|_n__n_I_c\n|___||__|###|____}\nO-O--O-O+++--O-O")
            while currentCart is not None:
                 print(currentCart)
                 currentCart = currentCart.next_cart   
    