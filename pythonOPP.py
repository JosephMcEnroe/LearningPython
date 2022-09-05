class Dog():
    
    def __init__(self,breed,name,spots): 
        #Attributes
        #We take in the argument
        #Assign it using Self
        self.breed = breed
        self.name = name
        #Expect True/False
        self.spots = spots
        
my_dog = Dog(breed = "Akita",name = "Aang",spots = True)
print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

