class MyHashSet:

    def __init__(self):
        self.data = []
        

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)
        
    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)
        
    def contains(self, key: int) -> bool:
        if key in self.data:
            return True
        
        
my_set = MyHashSet()

#add
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set.data)

#contains
print(my_set.contains(2))
print(my_set.contains(4))

#remove
my_set.remove(2)
print(my_set.data)