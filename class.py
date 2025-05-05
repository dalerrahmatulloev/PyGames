class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name = "noName", age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def __str__(self):
        return f"Cat: {self.name}, Age: {self.age}, Is happy: {self.isHappy}"

cat1 = Cat("Tom", 12, False)
cat2 = Cat("Ben", 3)
cat3 = Cat("Pit")
cat4 = Cat()

print(cat1, "\n", cat2, "\n", cat3, "\n", cat4)