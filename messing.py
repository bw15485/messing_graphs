#A Class is like an object constructor, or a "blueprint" for creating objects.
#Python method is like a function, except it is attached to an object.
#We call a method on an object, below we call average on object p1


class point(object):

    #all classes have an init function which is executed when the class is initiated
    def __init__(self, x, y): #the self parameter is a reference to the current instance of the class
        self.x = x
        self.y = y


   #Objects can also contain methods. Methods in objects are functions that belong to the object.
    def average(self):
        return (self.x+self.y)/2


#now we can use the class 'point' to create objects

p1 = point(8,9)
p1.x = 10 # you can modify properties of an object like this

print(p1.x)
print(p1.average())





























