# related to object oriented programming
# attributies and methods

class Action:
    def __init__(self, color, size, price, style="good fit"):
        self.color = color
        self.size = size
        self.price = price

    def offer(self):
        print(f"Good Offer is Coming {self.size.upper()} {self.color.upper()}Today!")
    
class ActionComplex(Action): 
     def __init__(self, color, size, price):
        self.color = color
        self.size = size
        self.price = price
        self.style="good fit"
     #def __init__(self, color, size, price):
       #Action().__init__(color, size, price)
       

if __name__ == "__main__":   
  
    action4 = Action(color="Green", size="XX-Large", price=100, style="good fit")
    print(action4.color, action4.size, action4.price)
    action4.offer()

    action5 = Action(color="Purple", size="X-Large", price=200)
    print(action5.color, action5.size, action5.price)
    action5.offer()

    action6= Action(color="Brown", size="Large", price=300, style="good fit")
    print(action6.color, action6.size, action6.price)
    action6.offer()

    action6= Action(color="Yellow", size="Medium", price=400)
    print(action6.color, action6.size, action6.price)
    action6.offer()

    action7= ActionComplex(color="Red", size="Small", price=500)
    print(action7.color, action7.size, action7.price)
    action7.offer()