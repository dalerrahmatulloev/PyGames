class Building:
    def __init__(self, year = None, city = None):
        self.year = year
        self.city = city

    def get(self):
        print(f"Year: {self.year}, City: {self.city}")

class House(Building):
    def __init__(self, year = None, city = None, quer = None):
        super().__init__(year, city)
        self.quer = quer
    
    def get(self):
        super().get()
        print(f"Quer: {self.quer}")

class Room(House):
    def __init__(self, year = None, city = None, quer = None, room = None):
        super().__init__(year, city, quer)
        self.room = room
    
    def get(self):
        super().get()
        print(f"Quer: {self.quer}, Room: {self.room}")

house = Room(2000, "New York", 200, "2 rooms")
house.get()

school = Building(1990, "Los Angeles")
school.get()

shop = Building(2010, "Chicago")
shop.get()